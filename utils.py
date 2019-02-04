import re


open_tag = re.compile(r'<(\w+).*?>')
close_tag = re.compile(r'</(.*?)>')


class InputError(Exception):
    pass


def find_all_tags(string):
    open_tags = list(open_tag.finditer(string))
    open_tags = [open_tag for open_tag in open_tags 
                 if not is_self_close_tag(open_tag)]
    close_tags = list(close_tag.finditer(string))
    all_tags = open_tags + close_tags
    all_tags.sort(key=lambda x: x.span())
    return all_tags


def tag_name(tag_obj):
    return tag_obj.group(1)


def empty_tag_name(tag_obj):
    return tag_name(tag_obj) == ''


def is_close_tag(tag_obj):
    """
    Test if the match object is a close tag. </> counts as a close tag.
    """
    return tag_obj.group().startswith('</')

def is_self_close_tag(tag_obj):
    """
    Test if the match object is a self-close tag. </> counts as a close tag.
    """
    return tag_obj.group().endswith('/>')


def partition_and_replace(string, all_tags):
    """
    Partition `string` at each </> according to `all_tags`. Complete the </> tag
    with its tag name. Return a new string without </>.

    Note: Self-close tags are not contained in argument `all_tags`.
    """
    start = 0
    tag_stack = []
    partitioned_replaced_strings = []
    for tag in all_tags:
        if is_close_tag(tag):
            if len(tag_stack) == 0:
                raise InputError('can not find open tag for {}'.
                    format(tag.group()))
            if is_close_tag(tag_stack[-1]):
                raise InputError('duplicated close tag {}'.format(
                    tag.group()))
            if tag_name(tag_stack[-1]) == tag_name(tag):
                tag_stack.pop()
            elif empty_tag_name(tag):
                # This is the main purpose of this plugin.
                end = tag.span()[1]
                string_slice = string[start:end]
                new_close_tag = '</{}>'.format(tag_name(tag_stack[-1]))
                new_string = string_slice.replace('</>', new_close_tag)
                partitioned_replaced_strings.append(new_string)
                start = end
                tag_stack.pop()
            else:
                raise InputError('open tag {} and close tag {} does not match'
                        .format(tag_stack[-1].group(), tag.group()))
        elif is_self_close_tag(tag):
            continue
        else:
            tag_stack.append(tag)
    if len(partitioned_replaced_strings) == 0:
        return string
    partitioned_replaced_strings.append(string[start:])
    return ''.join(partitioned_replaced_strings)


def complete_close_tag(string):
    all_tags = find_all_tags(string)
    new_string = partition_and_replace(string, all_tags)
    return new_string
