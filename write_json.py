import json
from collections import Counter

new_dict = Counter()

# 直接バージョン
new_dict['A'] = {'i': 1, 'j': 2}
new_dict['B'] = [{'X': 1, 'Y': 10}, {'X': 2, 'Y': 20}]
new_dict['C'] = 'あ'
print(new_dict)

# 順次挿入バージョン
# a_dict = Counter()
# a_dict['i'] = 1
# a_dict['j'] = 2
# new_dict['A'] = a_dict['j']

# b_list = list()
# b_list.append({'X': 1, 'Y': 10})
# b_list.append({'X': 2, 'Y': 20})
# new_dict['B'] = b_list

# new_dict['C'] = 'あ'

with open('data/test_new.json', 'w') as f:
    json.dump(new_dict, f, indent=2, ensure_ascii=False)
