from bleu import list_bleu
ref = ['it is a white cat .',
            'wow , this dog is huge .']
ref1 = ['This cat is white .',
            'wow , this is a huge dog .']
hyp = ['it is a white kitten .',
        'wowww , the dog is huge !']
hyp1 = ["it 's a white kitten .",
            'wow , this dog is huge !']
print(list_bleu([ref], hyp))
