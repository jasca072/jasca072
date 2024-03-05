yosh = int(input('Nechta yosh kiritasiz? '))

for yosh1 in range(yosh):
    yosh1 = int(input('Yoshingiz nechada? '))
    if yosh <= 12:
        print('Assalomu aleykum! Siz {} yoshdasiz! va siz bu o\'yinni o\'ynay olmaysiz'.format(yosh1))
    if yosh > 12:
        print('Rahmat! O\'yinga kirishingiz mumkin Chunki siz {} yoshdasiz'.format(yosh1))
