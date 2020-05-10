def fun(s, k):
    if not s:
        return None
    split = s.split()
    output = list()
    index = 0
    while index < len(split):
        new_element = split[index]
        if len(new_element) > k:
            return None
        temp = new_element
        new_index = index
        while len(temp) <= k and new_index < len(split):
            new_index += 1
            if new_index < len(split):
                temp += ' ' + split[new_index]
            if len(temp) <= k:
                new_element = temp
            else:
                break
        if new_index > index:
            index = new_index
        else:
            index += 1
        output.append(new_element)
    return output


if __name__ == '__main__':
    assert fun("encyclopedia and dog", 12) == ['encyclopedia', 'and dog']
    assert fun('the quick brown fox jumps over the lazy dog', 12) == ['the quick', 'brown fox', 'jumps over',
                                                                      'the lazy dog']

    input_str = "THESE TERMS AND CONDITIONS OF SERVICE (the Terms) ARE A LEGAL AND BINDING AGREEMENT BETWEEN YOU AND " \
                "NATIONAL GEOGRAPHIC governing your use of this site, www.nationalgeographic.com, which includes but " \
                "is not limited to products, software and services offered by way of the website such as the Video " \
                "Player, Uploader, and other applications that link to these Terms (the Site). Please review the " \
                "Terms fully before you continue to use the Site. By using the Site, you agree to be bound by the " \
                "Terms. You shall also be subject to any additional terms posted with respect to individual sections " \
                "of the Site. Please review our Privacy Policy, which also governs your use of the Site, " \
                "to understand our practices. If you do not agree, please discontinue using the Site. National " \
                "Geographic reserves the right to change the Terms at any time without prior notice. Your continued " \
                "access or use of the Site after such changes indicates your acceptance of the Terms as modified. It " \
                "is your responsibility to review the Terms regularly. The Terms were last updated on 18 July 2011. "
    assert fun(input_str, 80) == ['THESE TERMS AND CONDITIONS OF SERVICE (the Terms) ARE A LEGAL AND BINDING',
                                  'AGREEMENT BETWEEN YOU AND NATIONAL GEOGRAPHIC governing your use of this site,',
                                  'www.nationalgeographic.com, which includes but is not limited to products,',
                                  'software and services offered by way of the website such as the Video Player,',
                                  'Uploader, and other applications that link to these Terms (the Site). Please',
                                  'review the Terms fully before you continue to use the Site. By using the Site,',
                                  'you agree to be bound by the Terms. You shall also be subject to any additional',
                                  'terms posted with respect to individual sections of the Site. Please review our',
                                  'Privacy Policy, which also governs your use of the Site, to understand our',
                                  'practices. If you do not agree, please discontinue using the Site. National',
                                  'Geographic reserves the right to change the Terms at any time without prior',
                                  'notice. Your continued access or use of the Site after such changes indicates',
                                  'your acceptance of the Terms as modified. It is your responsibility to review',
                                  'the Terms regularly. The Terms were last updated on 18 July 2011.']
