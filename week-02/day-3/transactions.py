import xml.etree.ElementTree as et

def find_usd(file):
    xtree = et.parse(file)
    xroot = xtree.getroot()
    to_list = []
    from_list = []
    curr_list = []
    amount_list = []
    for root in xroot:
        from_list.append(root[0].text)
        to_list.append(root[1].text)
        amount_list.append(root[2].text)
        curr_list.append(root[2].attrib['currency'])
    for i in range(len(curr_list)):
        if curr_list[i] == 'USD':
            print(f'USD {amount_list[i]} from account {from_list[i]} is transferred to account {to_list[i]}.')


find_usd('transactions.xml')
