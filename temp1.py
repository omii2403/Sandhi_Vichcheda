def rule1(word, ans, temp, c):
    flag = True
    ch = [x for x in word]
    for i, x in enumerate(ch):
        if x == 'ा' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'ी' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'ू' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'ॄ' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'े' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'ो' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'र' and i<(len(ch)-2) and ch[i+1] == '्' and i > c and i<(len(ch)-1):
            flag = False
        if x == 'ल' and i<(len(ch)-2) and ch[i+1] == '्' and i > c:
            flag = False
        if x == 'ै' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'ौ' and i <(len(ch)-1) and i > c:
            flag = False
        if x == 'य' and i<(len(ch)-2) and i>0 and ch[i-1] == '्' and i > c:
            flag = False
        if x == 'व' and i <(len(ch)-1) and i>0 and ch[i-1] == '्' and i > c:
            flag = False
        if x == 'र' and i <(len(ch)-1) and i>0 and ch[i-1] == '्' and i > c:
            flag = False
        if x == 'य' and i<(len(ch)-2) and ch[i+1] in ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ'] and i > c:
            flag = False
        if x == 'व' and i<(len(ch)-2) and ch[i+1] in ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ'] and i > c:
            flag = False
        if x == 'ऽ' and i<(len(ch)-1) and i > c:
            flag = False
        if x in ['र'] and i <(len(ch)-2) and ch[i+1] in ['ु', 'ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ'] and i > c:
            flag = False
        if x in ['र'] and i <(len(ch)-2) and ch[i+1] in ['्'] and i > c:
            flag = False
        if x in ['र'] and i <(len(ch)-1) and i > c:
            flag = False
        if x in ['श'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['च','छ']:
            flag = False
        if x in ['ष'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['ट','ठ']:
            flag = False
        if x in ['स'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['त','थ']:
            flag = False
        if x in ['श'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['श']:
            flag = False
        if x in ['ष'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['ष']:
            flag = False
        if x in ['स'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['स']:
            flag = False
        if x in ['त'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
            flag = False
        if x in ['क'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
            flag = False
        if x in ['च'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
            flag = False
        if x in ['ट'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
            flag = False
        if x in ['प'] and i <(len(ch)-2) and i > c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
            flag = False
        if i > 0 and i == len(ch)-1 and i > c and (ch[i] == 'ध') and (ch[i-1] == '्') and (ch[i-2] in ['ग','ज','ड','द','ब']):
            flag = False
        if i > 0 and i<len(ch)-1 and i > c and i == len(ch)-2 and (ch[i] == 'ध') and (ch[i-1] == '्') and (ch[i-2] in ['ग','ज','ड','द','ब','क','च','प','त','ट']) and ch[i+1] in vowel_sym:
            flag = False
        if i<len(ch)-2 and i > c and ((x in ['ग','ज','ड','द','ब'] and (ch[i+1] in vowel_sym or ch[i+1] in sv_scwn)) or (x in ['ग','ज','ड','द','ब'] and ch[i+1] == '्' and ch[i+2] in sv_scwn)):
            flag = False
        if i<len(ch)-2 and i > c and x in ['ज'] and ch[i+1] in ['्'] and ch[i+2] in ['च','छ','ज','झ']:
            flag = False
        if i<len(ch)-2 and i > c and x in ['ड'] and ch[i+1] in ['्'] and ch[i+2] in ['ट','ठ','ड','ढ']:
            flag = False
            
    if flag:
        ans.append(temp.copy() + [word])
    else:
        for i, x in enumerate(ch):
            # (A) Dirgha Sandhi (दीर्घ   सन्धि)  (आ) is formed when (अ, आ) combines with (अ, आ)
            if x == 'ा' and i <(len(ch)-1) and i >= c:
                # print('ा')
                rule1(word, ans, temp, i+1)
                left_split = ch[:i]
                left_extra = ['', 'ा']
                right_extra = ['अ', 'आ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # (A) Dirgha Sandhi (दीर्घ   सन्धि) (ई) is formed when (इ, ई) combines with (इ, ई)
            if x == 'ी' and i <(len(ch)-1) and i >= c:
                # print('ी')
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['ि', 'ी']
                right_extra = ['इ', 'ई']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # (A) Dirgha Sandhi (दीर्घ   सन्धि)  (उ) is formed when (उ, ऊ) combines with (उ, ऊ)
            if x == 'ू' and i <(len(ch)-1) and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['ु', 'ू']
                right_extra = ['उ', 'ऊ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            #(A) Dirgha Sandhi (दीर्घ   सन्धि)  (ॠ) is formed when (ऋ, ॠ) combines with (ऋ, ॠ)
            if x == 'ॄ' and i <(len(ch)-1) and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['ृ', 'ॄ']
                right_extra = ['ऋ', 'ॠ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Guna Sandhi (गुण   सन्धि) (ए) is formed when (अ, आ) combines with (इ, ई)
            if x == 'े' and i <(len(ch)-1) and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['', 'ा']
                right_extra = ['इ', 'ई']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Guna Sandhi (गुण   सन्धि) B2. (ओ) is formed when (अ, आ) combines with (उ, ऊ)
            if x == 'ो' and i <(len(ch)-1) and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['', 'ा']
                right_extra = ['उ', 'ऊ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Guna Sandhi (गुण   सन्धि) B3. (अर्) is formed when (अ, आ) combines with (ऋ, ॠ)
            if x == 'र' and i<(len(ch)-2) and ch[i+1] == '्' and i >= c and i<(len(ch)-1):
                # print("aagad r adadho chhe")
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['', 'ा']
                right_extra = ['ऋ', 'ॠ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Guna Sandhi (गुण   सन्धि) B4. (अल्) is formed when (अ, आ) combines with (ऌ)
            if x == 'ल' and i<(len(ch)-2) and ch[i+1] == '्' and i >= c:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['', 'ा']
                right_extra = ['ऌ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Vrddhi Sandhi (वृद्धि   सन्धि) C1. (ऐ) is formed when (अ, आ) combines with (ए)
            if x == 'ै' and i <(len(ch)-1) and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['', 'ा']
                right_extra = ['ए','ऐ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            #  Vrddhi Sandhi (वृद्धि   सन्धि) C2. (औ) is formed when (अ, आ) combines with (ओ)
            if x == 'ौ' and i <(len(ch)-1) and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['', 'ा']
                right_extra = ['ओ', 'औ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Yana Sandhi (यण्   सन्धि) D1. (इ, ई) changes to (य्) when followed by (dissimilar vowel).
            if x == 'य' and i<(len(ch)-2) and i>0 and ch[i-1] == '्' and i >= c:
                # print("y pela adadhu")
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-1]
                left_extra = ['ि', 'ी']
                right_extra = list(yana_D1_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Yana Sandhi (यण्   सन्धि) D2. (उ, ऊ) changes to (व्) when followed by (dissimilar vowel).
            if x == 'व' and i <(len(ch)-1) and i>0 and ch[i-1] == '्' and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-1]
                left_extra = ['ु', 'ू']
                right_extra = list(yana_D2_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Yana Sandhi (यण्   सन्धि) D3. (ऋ, ॠ) changes to (र्) when followed by (dissimilar vowel).
            if x == 'र' and i <(len(ch)-1) and i>0 and ch[i-1] == '्' and i >= c:
                # print("r pela adadhu")
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-1]
                left_extra = ['ृ', 'ॄ']
                right_extra = list(yana_D3_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Ayadi Sandhi (अयादि   सन्धि) E1. (ए) changes to (अय्) or (अ) when followed by (vowel-अ).
            if x == 'य' and i<(len(ch)-2) and ch[i+1] in ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ'] and i >= c:
                # print("y pachhi kaik")
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['े']
                right_extra = list(yana_D3_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Ayadi Sandhi (अयादि   सन्धि) E2. (ओ) changes to (अव्) or (अ) when followed by (vowel-अ).
            if x == 'व' and i<(len(ch)-2) and ch[i+1] in ['ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ'] and i >= c:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['ो']
                right_extra = list(yana_D3_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Ayadi Sandhi (अयादि   सन्धि) E3. (ए) remains unchanged when followed by (अ) but (अ) changes to (avagraha).
            if x == 'ऽ' and i<(len(ch)-1) and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = ['']
                right_extra = ['अ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Ayadi Sandhi (अयादि   सन्धि) E5. (ऐ) changes to (आय्) or (आ) when followed by (vowel).
            if x == 'य' and i>0 and ch[i-1] == 'ा' and i >= c  and i<(len(ch)-1):
                # print("y pela kano")
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-1]
                left_extra = ['ै']
                right_extra = list(yana_D3_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Ayadi Sandhi (अयादि   सन्धि) E6. (औ) changes to (आव्) or (आ) when followed by (vowel).
            if x == 'व' and i>0 and ch[i-1] == 'ा' and i >= c  and i<(len(ch)-1):
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-1]
                left_extra = ['ौ']
                right_extra = list(yana_D3_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Visarga to ओ (अ & visarga) standing for (अस्) changes to (ओ+avagraha) when followed by (अ). Here visarga changes to ओ and the अ of the second word changes to (avagraha).
            if x == 'ऽ' and i>0 and ch[i-1] == 'ो' and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-1]
                left_extra = [':']
                right_extra = ['अ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Visarga to ओ (अ & visarga) standing for (अस्) followed by a (soft consonant) changes to (ओ).
            if x in ['ो'] and i <(len(ch)-1) and ch[i+1] == ' ' and i >= c:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Visarga to र् C1. (visarga) after any (vowel except अ or आ) changes to र् when followed by a (vowel or soft consonant except र्)
            if x in ['र'] and i <(len(ch)-2) and ch[i+1] in ['ु', 'ा', 'ि', 'ी', 'ु', 'ू', 'े', 'ै', 'ो', 'ौ'] and i >= c:
                # print("r pachhi kaik")
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = list('' + yana_D3_helper(ch[i+1]))
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            if x in ['र'] and i <(len(ch)-2) and ch[i+1] in ['्'] and i >= c:
                # print("r pachhi adadhu")
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            if x in ['र'] and i <(len(ch)-1) and i >= c:
                # print("r pachhi kaibi")
                rule1(word,ans,temp,i+1)
                left_split = ch[:i]
                left_extra = list(yana_D3_helper(ch[i-1]) + ':')
                right_extra = ['अ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Visarga to श्, ष्, स् D1. (visarga) changes to (श्) (p sb) when followed by (च् or छ्)
            if x in ['श'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['च','छ']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # (visarga) changes to (ष्) (c sb) when followed by (ट् or ठ्) (c hc).
            if x in ['ष'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['ट','ठ']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # (visarga) changes to (स्) (d sb) when followed by (त् or थ्) (d hc).
            if x in ['स'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['त','थ']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Visarga to श्, ष्, स् D4. (visarga) after a (vowel) optionally changes to (श्) (p sb) when followed by (श्) (p sb).
            if x in ['श'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['श']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Visarga to श्, ष्, स् D5. (visarga) after a (vowel) optionally changes to (ष्) (c sb) when followed by (ष्) (c sb).
            if x in ['ष'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['ष']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Visarga to श्, ष्, स् D6. (visarga) after a (vowel) optionally changes to (स्) (d sb) when followed by (स्) (d sb).
            if x in ['स'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['स']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = [':']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # Consonant Sandhi Rule: (A) Soft Consonant to Hard Consonant (1st of class) A1. (Class soft consonant except nasal) followed by a (hard consonant) changes to (1st consonant of class).
            if x in ['त'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['द्','ध्']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            if x in ['क'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['ग्','घ्']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            if x in ['च'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['ज्','झ्']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            if x in ['ट'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['ड्','ढ्']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            if x in ['प'] and i <(len(ch)-2) and i >= c and ch[i+1] in ['्'] and ch[i+2] in ['क','ख','च','छ','ट','ठ','त','थ','प','फ','श','ष','स']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['ब्','भ्']
                right_extra = ['']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # (Verbal base) followed by (terminations beginning with त् or थ्) changes to the (corresponding non-aspirate and ध्).
            if i > 0 and i >= c and i == len(ch)-1 and (ch[i] == 'ध') and (ch[i-1] == '्') and (ch[i-2] in ['ग','ज','ड','द','ब','क','च','प','त','ट']):
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-2]
                left_extra = list(helper1(ch[i-2]))
                right_extra = ['त','थ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k]
                        rule1(''.join(right_split), ans, new_temp, 0)
            if i > 0 and i >= c and i<len(ch)-1 and i == len(ch)-2 and (ch[i] == 'ध') and (ch[i-1] == '्') and (ch[i-2] in ['ग','ज','ड','द','ब','क','च','प','त','ट']) and ch[i+1] in vowel_sym:
                rule1(word,ans,temp,i+1)
                left_split = ch[:i-2]
                left_extra = list(helper1(ch[i-2]))
                right_extra = ['त','थ']
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+1:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # (Class hard consonant) followed by a (vowel, semivowel or class soft consonant except nasal) changes to the (3rd consonant of class).
            if i<len(ch)-2 and i >= c and ((x in ['ग','ज','ड','द','ब'] and (ch[i+1] in vowel_sym or ch[i+1] in sv_scwn)) or (x in ['ग','ज','ड','द','ब'] and ch[i+1] == '्' and ch[i+2] in sv_scwn)):
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = (helperB1(x))
                right_extra = ['']
                if ch[i+1] in vowel_sym: right_extra = yana_D3_helper(ch[i+1])
                # else: right_extra = list(ch[i+2])
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            # e1. (Dental class hard consonant) followed by (Palatal class soft consonant except nasal) changes to the (3rd of the Palatal class).
            if i<len(ch)-2 and i >= c and x in ['ज'] and ch[i+1] in ['्'] and ch[i+2] in ['च','छ','ज','झ']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['त्','थ्']
                right_extra = ['']
                if ch[i+1] in vowel_sym: right_extra = yana_D3_helper(ch[i+1])
                # else: right_extra = list(ch[i+2])
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)
            #  (Dental class hard consonant) followed by (Cerebral class soft consonant except nasal) changes to the (3rd of the Cerebral class).
            if i<len(ch)-2 and i >= c and x in ['ड'] and ch[i+1] in ['्'] and ch[i+2] in ['ट','ठ','ड','ढ']:
                rule1(word,ans,temp,i+2)
                left_split = ch[:i]
                left_extra = ['त्','थ्']
                right_extra = ['']
                if ch[i+1] in vowel_sym: right_extra = yana_D3_helper(ch[i+1])
                # else: right_extra = list(ch[i+2])
                for j in left_extra:
                    for k in right_extra:
                        new_temp = temp.copy() + [''.join(left_split) + j]
                        right_split = [k] + ch[i+2:]
                        rule1(''.join(right_split), ans, new_temp, 0)



def helperB1(c):
    if c == 'ग': return ['क्','ख्']
    elif c == 'ज': return ['च्','छ्']
    elif c == 'ड': return ['ट्','ठ्']
    elif c == 'द': return ['त्','थ्']
    elif c == 'ब': return ['प्','फ्']
            
def helper1(c):
    if c == 'ग': return 'घ'
    elif c == 'ज': return 'झ'
    elif c == 'ड': return 'ढ'
    elif c == 'द': return 'ध'
    elif c == 'ब': return 'भ'
    elif c == 'क': return 'ख'
    elif c == 'च': return 'छ'
    elif c == 'ट': return 'ठ'
    elif c == 'त': return 'थ'
    elif c == 'प': return 'फ'
            
def yana_D1_helper(c):
    if c == 'ा' : return 'आ'
    elif c == 'ु' : return 'उ'
    elif c == 'ू' : return 'ऊ'
    elif c == 'े' : return 'ए'
    elif c == 'ै' : return 'ऐ'
    elif c == 'ो' : return 'ओ'
    elif c == 'ौ' : return 'औ'
    return 'अ'

def yana_D2_helper(c):
    if c == 'ा' : return 'आ'
    elif c == 'े' : return 'ए'
    elif c == 'ै' : return 'ऐ'
    elif c == 'ो' : return 'ओ'
    elif c == 'ौ' : return 'औ'
    elif c == 'ि' : return 'इ'
    elif c == 'ी' : return 'ई'
    return 'अ'

def yana_D3_helper(c):
    if c == 'ा' : return 'आ'
    elif c == 'ु' : return 'उ'
    elif c == 'ू' : return 'ऊ'
    elif c == 'े' : return 'ए'
    elif c == 'ै' : return 'ऐ'
    elif c == 'ो' : return 'ओ'
    elif c == 'ौ' : return 'औ'
    elif c == 'ि' : return 'इ'
    elif c == 'ी' : return 'ई'
    return 'अ'


global vowel_sym
global vowels
global sv_scwn
if __name__ == "__main__":
    word1 = "कर्मण्येवाधिकारस्ते"
    vowels = ['अ', 'आ', 'इ', 'ई', 'उ' , 'ऊ', 'ऋ', 'ॠ', 'ए', 'ऐ', 'ओ', 'औ']
    vowel_sym = ['ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'े', 'ै', 'ो', 'ौ']
    sv_scwn = ['य', 'र', 'ल', 'व', 'ग','ज','ड','द','ब','घ', 'झ','ढ','ध','भ']
    ans = []
    temp = []
    rule1(word1, ans, temp, 0)
    ch = [x for x in word1]
    print(ch)
    with open("output.txt", "w", encoding="utf-8") as file:
        for sublist in ans:
            file.write(" ".join(sublist) + "\n")


    vocabulary = [" "]

    # Read vocabulary from file
    with open("NLP_Sandhi_viched.txt", "r", encoding="utf-8") as vocab_file:
        for line in vocab_file:
            word = line.strip()
            if word:
                vocabulary.append(word)
    perfect_sandhi = None

    with open("output.txt", "r", encoding="utf-8") as file:
        content = file.read().splitlines()

    for line in content:
        all_words_match = True
        matching_words = []
        for word in line.split():
            word = word.strip()
            if word not in vocabulary:
                all_words_match = False
                break
            else:
                matching_words.append(word)
        if all_words_match:
            perfect_sandhi = " + ".join(matching_words)
            break

    if perfect_sandhi:
        print("Perfect sandhi found:", perfect_sandhi)
    else:
        print("No perfect sandhi found.")
    # print(vocabulary)
