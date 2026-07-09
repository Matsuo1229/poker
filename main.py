import pygame
import sys
import asyncio
import random

WHITE = (255,255,255)
BLACK = (0,0,0)

idx = 0

sha=("スペードの","クラブの","ダイヤの","ハートの")
num=("2","3","4","5","6","7","8","9","10","J","Q","K","A")

async def hand(): #手札の配布
    global shape,number,n_1,n_2,n_3,n_4,n_5,s_1,s_2,s_3,s_4,s_5,result,gazou,tag,file,illust_1,illust_2,illust_3,illust_5,illust_4
    global rireki,a
    for i in range(5):
        shape=random.choice(["スペードの","クラブの","ハートの","ダイヤの"])
        number=random.choice(num)

        if i==0:
            s_1=shape
            n_1=number
            await check()

        if i==1:
            while shape==s_1 or number==n_1:
               shape=random.choice(["スペードの","クラブの","ハートの","ダイヤの"])
               number=random.choice(["A","2","3","4","5","6","7","8","9","10","J","Q","K"])
               s_2=shape
               n_2=number
             
            s_2=shape
            n_2=number
            await check()

        if i==2:
            while shape==s_1 or shape==s_2 and number==n_1 or number==n_2:
                shape=random.choice(["スペードの","クラブの","ハートの","ダイヤの"])
                number=random.choice(["A","2","3","4","5","6","7","8","9","10","J","Q","K"])
                s_3=shape
                n_3=number
        
            s_3=shape
            n_3=number
            await check()

        if i==3:
            while shape==s_1 and number==n_1 or shape==s_2 and  number==n_2 or shape==s_3 and number==n_3:
                shape=random.choice(["スペードの","クラブの","ハートの","ダイヤの"])
                number=random.choice(["A","2","3","4","5","6","7","8","9","10","J","Q","K"])
                s_4=shape
                n_4=number
    
            s_4=shape
            n_4=number
            await check()     

        if i==4:
            while shape==s_1 and number==n_1 or shape==s_2 and  number==n_2 or shape==s_3 and number==n_3 or shape==s_4 or number==n_4:
                shape=random.choice(["スペードの","クラブの","ハートの","ダイヤの"])
                number=random.choice(["A","2","3","4","5","6","7","8","9","10","J","Q","K"])
                s_5=shape
                n_5=number
        
            s_5=shape
            n_5=number
            await check()

    rireki=[s_1+n_1,s_2+n_2,s_3+n_3,s_4+n_4]
    await asyncio.sleep(0)


async def change(): #カードの交換
    global shape,number,n_1,n_2,n_3,n_4,n_5,s_1,s_2,s_3,s_4,s_5,result,gazou,tag,file,illust_1,illust_2,illust_3,illust_5,illust_4
    global rireki,a
    

          
    canvas.update()            
    c()
    await asyncio.sleep(0)

async def c():
    pare=0
    tc=0
    fc=0
    st=0
    fr=0
    
    global n_1,n_2,n_3,n_4,n_5,s_1,s_2,s_3,s_4,s_5,result
    
    result="ざんねんでした～www"
    if n_1==n_2:
        pare=pare+1
        if n_2==n_3:
            tc=tc+1
            if n_3==n_4:
                fc=fc+1
            if n_3==n_5:
                fc=fc+1
        
        if n_2==n_4:
            tc=tc+1
            if n_4==n_5:
                fc=fc+1

    if n_1==n_3:
        pare=pare+1
        if n_3==n_4:
            tc=tc+1
            if n_4==n_5:
                fc=fc+1
            if n_3==n_5:
                tc=tc+1
    if n_1==n_4:
        pare=pare+1
        if n_4==n_5:
            tc=tc+1
        
    if n_1==n_5:
        pare=pare+1
    if n_2==n_3:
        pare=pare+1
        if n_3==n_4:
            tc=tc+1
            if n_4==n_5:
                fc=fc+1
        if n_3==n_5:
            tc=tc+1
        
    if n_2==n_4:
        pare=pare+1
        if n_4==n_5:
            tc=tc+1
    if n_2==n_5:
        pare=pare+1
    if n_3==n_4:
        pare=pare+1
        if n_4==n_5:
            tc=tc+1
    if n_3==n_5:
        pare=pare+1
    if n_4==n_5:
        pare=pare+1

    if pare==1:
        result="ワンペア"

    if pare==2:
        result="ツーペア"


    if n_1==n_2 and n_1==n_3 or n_1==n_2 and n_1==n_4 or n_1==n_2 and n_1==n_5:
        result="スリーカード"

    if n_1==n_3 and n_1==n_4 or n_1==n_3 and n_1==n_5 or n_1==n_4 and n_1==n_5 or n_2==n_3 and n_2==n_4 or n_2==n_3 and n_2==n_5 or n_3==n_4 and n_3==n_5:
        result="スリーカード"

    for i in range(9):
        if num[i] in [n_1,n_2,n_3,n_4,n_5]:
            if num[i+1] in [n_1,n_2,n_3,n_4,n_5]:
                if num[i+2] in [n_1,n_2,n_3,n_4,n_5]:
                    if num[i+3] in [n_1,n_2,n_3,n_4,n_5]:
                        if num[i+4] in [n_1,n_2,n_3,n_4,n_5]:
                            st=st+1
                            lsf=num[i]
                            result="ストレート"

    if s_1==s_2==s_3==s_4==s_5:
        fr=fr+1
        result="フラッシュ"

    if pare>=3 and tc>=1:
        result="フルハウス"
 
    if fc==1:
        result="フォーカード"

    if st>=1:
        if fr>=1:
            result="ストレートフラッシュ"
            if lsf=="10":
                result="ロイヤルストレートフラッシュ"
    await asyncio.sleep(0)

a=[None]*5
async def check(): #カードのイメージの判別と記録
    global a
    global shape,number,gazou
    if shape==sha[0]:
        if number==num[0]:
            gazou="torannpu-illust2.png"
        if number==num[1]:
            gazou="torannpu-illust3.png"
        if number==num[2]:
            gazou="torannpu-illust4.png"
        if number==num[3]:
            gazou="torannpu-illust5.png"
        if number==num[4]:
            gazou="torannpu-illust6.png"
        if number==num[5]:
            gazou="torannpu-illust7.png"
        if number==num[6]:
            gazou="torannpu-illust8.png"
        if number==num[7]:
            gazou="torannpu-illust9.png"
        if number==num[8]:
            gazou="torannpu-illust10.png"
        if number==num[9]:
            gazou="torannpu-illust11.png"
        if number==num[10]:
            gazou="torannpu-illust12.png"
        if number==num[11]:
            gazou="torannpu-illust13.png"
        if number==num[12]:
            gazou="torannpu-illust1.png"

    if shape==sha[1]:
        if number==num[0]:
            gazou="torannpu-illust15.png"
        if number==num[1]:
            gazou="torannpu-illust16.png"
        if number==num[2]:
            gazou="torannpu-illust17.png"
        if number==num[3]:
            gazou="torannpu-illust18.png"
        if number==num[4]:
            gazou="torannpu-illust19.png"
        if number==num[5]:
            gazou="torannpu-illust20.png"
        if number==num[6]:
            gazou="torannpu-illust21.png"
        if number==num[7]:
            gazou="torannpu-illust22.png"
        if number==num[8]:
            gazou="torannpu-illust23.png"
        if number==num[9]:
            gazou="torannpu-illust24.png"
        if number==num[10]:
            gazou="torannpu-illust25.png"
        if number==num[11]:
            gazou="torannpu-illust26.png"
        if number==num[12]:
            gazou="torannpu-illust14.png"

    if shape==sha[2]:
        if number==num[0]:
            gazou="torannpu-illust28.png"
        if number==num[1]:
            gazou="torannpu-illust29.png"
        if number==num[2]:
            gazou="torannpu-illust30.png"
        if number==num[3]:
            gazou="torannpu-illust31.png"
        if number==num[4]:
            gazou="torannpu-illust32.png"
        if number==num[5]:
            gazou="torannpu-illust33.png"
        if number==num[6]:
            gazou="torannpu-illust34.png"
        if number==num[7]:
            gazou="torannpu-illust35.png"
        if number==num[8]:
            gazou="torannpu-illust36.png"
        if number==num[9]:
            gazou="torannpu-illust37.png"
        if number==num[10]:
            gazou="torannpu-illust38.png"
        if number==num[11]:
            gazou="torannpu-illust39.png"
        if number==num[12]:
            gazou="torannpu-illust27.png"

    if shape==sha[3]:
        if number==num[0]:
            gazou="torannpu-illust41.png"
        if number==num[1]:
            gazou="torannpu-illust42.png"
        if number==num[2]:
            gazou="torannpu-illust43.png"
        if number==num[3]:
            gazou="torannpu-illust44.png"
        if number==num[4]:
            gazou="torannpu-illust45.png"
        if number==num[5]:
            gazou="torannpu-illust46.png"
        if number==num[6]:
            gazou="torannpu-illust47.png"
        if number==num[7]:
            gazou="torannpu-illust48.png"
        if number==num[8]:
            gazou="torannpu-illust49.png"
        if number==num[9]:
            gazou="torannpu-illust50.png"
        if number==num[10]:
            gazou="torannpu-illust51.png"
        if number==num[11]:
            gazou="torannpu-illust52.png"
        if number==num[12]:
            gazou="torannpu-illust40.png"

    a[i] = gazou
    await asyncio.sleep(0)


async def main():
    
    global shape,number,n_1,n_2,n_3,n_4,n_5,s_1,s_2,s_3,s_4,s_5,result,gazou,tag,file,illust_1,illust_2,illust_3,illust_5,illust_4,idx
    global rireki,a
    
    pygame.init()
    pygame.display.set_caption("poker")
    screen = pygame.display.set_mode((1100,800))
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 80)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        key = pygame.key.get_pressed()


        if idx == 0: #タイトル画面
            screen.fill(WHITE)

            txt = font.render("Press Space",True,WHITE)
            screen.blit(txt, [300,500])
            if key[pygame.K_SPACE] == 1: #ここらに画像はりたい
                 idx = 2

#        elif idx == 1:
#            bg.screen.fill(BLACK)
#            display_button("START", 15, BLACK, 400, 400, 30, , , , )#画像などが不足（idx = 2）まだ書いていない

            
        elif idx == 2:
            screen.fill(WHITE)
            await hand()
            illust_1 = pygame.image.load(a[4])
            illust_2 = pygame.image.load(a[3])
            illust_3 = pygame.image.load(a[2])
            illust_4 = pygame.image.load(a[1])
            illust_5 = pygame.image.load(a[0])

            bgillust_1 = pygame.image.load(a[4])
            bgillust_2 = pygame.image.load(a[3])
            bgillust_3 = pygame.image.load(a[2])
            bgillust_4 = pygame.image.load(a[1])
            bgillust_5 = pygame.image.load(a[0])

            screen.blit(illust_1, [50,400])
            screen.blit(illust_2, [250,400])
            screen.blit(illust_3, [450,400])
            screen.blit(illust_4, [650,400])
            screen.blit(illust_5, [850,400])

            btn_1 = screen.blit

            pygame.display.update()

            idx = 3

        elif idx == 3:

            pygame.display.flip()#AIによる追加
            clock.tick(10)
            await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())
