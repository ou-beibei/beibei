'我的主页'
import streamlit as st
from PIL import Image
#from collections import Counter
from time import *

page = st.sidebar.radio(':orange[_我的首页:sunglasses:_]',['我的兴趣推荐','我的图片处理工具','我的智慧词典','我的留言区','我的成分复杂的图鉴','好用小工具'])
def page_1():
    st.title('_这是我的兴趣推荐👇_')
    tab1,tab2,tab3 = st.tabs(['牢大','饮料涨价','老鼠会sing'])
    with tab1:
        with open('seeyouagain.mp3','rb') as f:
            my_mp3 = f.read()
        st.audio(my_mp3,format = 'audio/mp3',start_time = 0)
        st.write(':blue[牢大我想你了！]')
        st.image('冰红茶.jpg')
    with tab2:
        st.write(':orange[为什么最近总有东西要涨价？我的饮料怎么更贵了！]')
        st.image('生活.jpeg')
    with tab3:
        st.write(':red[震惊！老鼠会唱歌！]')
        st.image('悲伤鼠鼠.jpg')
        with open('悲伤鼠鼠唱歌.mp3','rb') as f:
            sad_mouse_mp3 = f.read()
        st.audio(sad_mouse_mp3,format = 'audio/mp3',start_time = 0)
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
    
def page_2():
    st.title(":sunglasses:图片处理小程序:sunglasses:")
    uploaded_file = st.file_uploader('图片上传:sunglasses:',type=['png','jpeg','jpg'])
    tab1,tab5,tab6,tab2,tab3,tab4 = st.tabs(['调色调1','调色调2','调色调3','反色调','像素化','神秘更改'])
    with tab1:
        col1,col2 = st.columns([1,1])
        if uploaded_file:
            img_1 = Image.open(uploaded_file)
            with col1:
                st.image(img_1)
            with col2:
                st.image(change_img(img_1,1,0,2))
    with tab5:
        col1,col2 = st.columns([1,1])
        if uploaded_file:
            img_1 = Image.open(uploaded_file)
            with col1:
                st.image(img_1)
            with col2:
                st.image(change_img(img_1,0,2,1))
    with tab6:
        col1,col2 = st.columns([1,1])
        if uploaded_file:
            img_1 = Image.open(uploaded_file)
            with col1:
                st.image(img_1)
            with col2:
                st.image(change_img(img_1,2,1,0))
    with tab2:
        col1,col2 = st.columns([1,1])
        if uploaded_file:
            img_2 = Image.open(uploaded_file)
            with col1:
                st.image(img_2)
            with col2:
                st.image(fan_img(img_2))
    with tab3:
        col1,col2 = st.columns([1,1])
        st.subheader(':red[该功能被神秘的力量报废了！]')
        # if uploaded_file:
        #     img_3 = Image.open(uploaded_file)
        #     with col1:
        #         st.image(img_3)
        #     with col2:
        #         st.image(xiang_img(img_3))
    with tab4:
        col1,col2 = st.columns([1,1])
        if uploaded_file:
            img_4 = Image.open(uploaded_file)
            with col1:
                st.image(img_4)
            with col2:
                st.image(daxiao_img(img_4))
    
def page_3():
    st.title('awa_智慧词典📖_awa')
    tab1,tab2,tab3 = st.tabs(['查单词&错题本','单词秒杀','记单词'])
    with tab1:
        st.write('__来查单词吧！__')
        with open('words_space.txt','r',encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        words_dict = {}
        for i in words_list:
            words_dict[i[1]] = [int(i[0]),i[2]]
        with open('check_out_times.txt','r',encoding='utf-8') as f:
            times_list = f.read().split('\n')
        for i in range(len(times_list)):
            times_list[i] = times_list[i].split('#')
        times_dict = {}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
        word = st.text_input('请输入要查询的单词：')
        if word in words_dict:
            st.write(words_dict[word])
            n = words_dict[word][0]
            if n in times_dict:
                times_dict[n] += 1
            else:
                times_dict[n] = 1
            with open('check_out_times.txt','w',encoding='utf-8') as f:
                message = ''
                for k,v in times_dict.items():
                    message += str(k) + '#' + str(v) + '\n'
                message = message[:-1]
                f.write(message)
            a = str(times_dict[n])
            st.write(f':blue[_这个单词一共被查阅了{a}次_]')
            if word == 'Man':
                st.balloons()
                with open('SeeYouAgain.mp3','rb') as f:
                    man_mp3 = f.read()
                st.audio(man_mp3,format = 'audio/mp3',start_time = 0)
            if word == 'python':
                st.snow()
                st.write(':red[_这是本网站的制作器_]')
                st.code('''这是一行Python代码
                        print('千万别输入Man')''')
            if word == 'ikun':
                st.balloons()
                st.write(':red[_你是真爱粉吗？_]')
                st.image('小坤佩奇.png')
            if word == 'oubeibei':
                st.write(':red[不是，你怎么知道的]')
                st.image('新鲜哥猫.jpg')
            if word == 'Kobe Bryant' or word == 'Kobe':
                st.balloons()
                st.image('冰红茶.jpg')
                with open('SeeYouAgain.mp3','rb') as f:
                    man_mp3 = f.read()
                st.audio(man_mp3,format = 'audio/mp3',start_time = 0)
            if word == 'Technoblade':
                st.write(':red[_Technoblade never dies!_]')
            if word == 'dream':
                st.image('dream.png')
        elif word not in words_dict and word:
            st.write(':blue[_未找到该单词，请重新输入_]')
    with tab2:
        with open('words_space.txt','r',encoding='utf-8') as f:
            words_list = f.read().split('\n')
        for i in range(len(words_list)):
            words_list[i] = words_list[i].split('#')
        st.write(':blue[__单词秒杀四选一，可以开始了吗？__]')
        if st.button('我准备好了！'):
            pass
            # words_l = []
            # words = st.progress(0, '准备开始单词记忆挑战！')
            # for i in range(4, 0, -1):
            #     sleep(2)
            #     words.progress(i*25, str(w))
            #     words_l.append(w)
            # sleep(3)
            # words.progress(0, '开始回答吧！')
        st.subheader(':red[编程小老鼠正在加班，敬请期待！]')
        # if words_l:
        #     w = choice(words_l)
        #     st.write(' ')
        #     wo= st.text_input(f'{w[2]}的英文是？')
    
        #     if w[1] == wo:
        #         st.write(':red[对了，great!]')
        #     else:
        #         st.write('错了！此词记为查询单词')
        #         with open('check_out_times.txt','r',encoding='utf-8') as f:
        #             times_list = f.read().split('\n')
        #         for i in range(len(times_list)):
        #             times_list[i] = times_list[i].split('#')
        #         times_dict = {}
        #         for i in times_list:
        #             times_dict[int(i[0])] = int(i[1])
        #         n = w[0]
        #         if n in times_dict:
        #             times_dict[n] += 1
        #         else:
        #             times_dict[n] = 1
    with tab3:
        word= st.text_input('__你要记什么单词？__')
        st.write('此词记为查询单词并显示在标题下方')
        st.subheader(':red[编程小老鼠正在加班，敬请期待！]')
            

    st.write('----')
    ex = st.toggle('开启错题本')
    if ex:
        for j in times_dict.keys():
            for i in words_dict.keys():
                if times_dict[j] > 2 and j == words_dict[i][0]:
                    st.write(f'{i}  {words_dict[i][1]}:一共查了{times_dict[j]}次')
                    break
                else:
                    pass
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_4():
    st.title('🪐我的留言区🪐')
    st.write(':red[_注意：在留言完后将留言人更改即可查看自己的留言_]')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '坤坤':
            with st.chat_message('🐥'):
                st.write(i[1],':',i[2])
        elif i[1] == '老八':
            with st.chat_message('💩'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '科比':
            with st.chat_message('🏀'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '贝贝':
            with st.chat_message('👌'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '小黑子':
            with st.chat_message('🐔'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '小老鼠':
            with st.chat_message('🐀'):
                st.text(i[1]+':'+i[2])
        elif i[1] == '普通人':
            with st.chat_message('🙃'):
                st.text(i[1]+':'+i[2])
        elif i[1] == 'coke':
            with st.chat_message('😺'):
                st.text(i[1]+':'+i[2])
    name = st.selectbox('我是……',['坤坤','老八','科比','贝贝','小黑子','小老鼠','普通人','coke'])
    new_message = st.text_input('我想说的话……')
    if st.button('🪑留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
    with open('leave_messages.txt','w',encoding='utf-8') as f:
        message = ''
        for i in messages_list:
            message += i[0]+'#'+i[1]+'#'+i[2]+'\n'
        message = message[:-1]
        f.write(message)
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')
def page_5():
    st.title(':purple[这是个《正经》的图鉴🤪]')
    tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8 = st.tabs(['小坤佩奇','恶搞坤坤','冰红茶科比','劲凉冰红茶梅西','悲伤鼠鼠','新鲜哥猫','奸商','流浪栓绳'])
    st.write('———————————————————我是分界线———————————————————')
    tab9,tab10,tab11,tab12,tab13 = st.tabs(['废石三兄弟','臭猫','《虾》','白色巨型僵尸','分界线'])
    with tab1:
        st.write(':blue[小坤佩奇]')
        st.image('小坤佩奇.png')
    with tab2:
        st.write('恶搞坤坤')
        st.image('恶搞坤坤.png')
    with tab3:
        st.write('冰红茶科比')
        st.image('冰红茶.jpg')
    with tab4:
        st.write('劲凉冰红茶梅西')
        st.image('劲凉冰红茶.png')
    with tab5:
        st.write(':blue[悲伤鼠鼠]')
        st.image('悲伤鼠鼠.jpg')
        st.write('它会唱会儿歌')
        with open('悲伤鼠鼠唱歌.mp3','rb') as f:
            sad_mouse_mp3 = f.read()
        st.audio(sad_mouse_mp3,format = 'audio/mp3',start_time = 0)
    with tab6:
        st.write('新鲜哥猫')
        st.image('新鲜哥猫.jpg')
    with tab7:
        st.write('奸商')
        st.image('Plains_Villager_Base.png')
        st.write(':red[打折扣吧，只要一组绿宝石就给两个甜菜根]')
    with tab8:
        st.write('流浪栓绳')
        st.image('Wandering_Trader_JE1_BE1.png')
        st.write(':red[我比上一个便宜，我两个绿宝石换一个苔藓块]')
    with tab9:
        st.write('废石三兄弟')
        st.image('废石三兄弟.png')
        st.write(':red[你的背包看起来还可以在装点]')
    with tab10:
        st.write('臭猫')
        st.image('臭猫.jpg')
        st.write(':red[我不会动，但我自带bgm]')
        with open('臭猫bgm.mp3','rb') as f:
            cat_mp3 = f.read()
        st.audio(cat_mp3,format = 'audio/mp3',start_time = 0)
    with tab11:
        st.write('《虾》')
        st.image('虾.jpg')
    with tab12:
        st.write(':blue[白色巨型僵尸]')
        st.image('白色巨型僵尸.png')
        st.write(':red[《村庄祸害者，他永远不会还手》]')
    with tab13:
        st.write(':blue[此生物以这种形式：]')
        st.write(' ')
        st.write('——————————————————我是分界线———————————————————')
        st.write(' ')
        st.write(':blue[或这种形式：]')
        st.write(' ')
        st.write('----')
        st.write(' ')
        st.write(':blue[出现，有时也以这种形式：]')
        st.write(' ')
        st.write('————————————————————我也是有底线的————————————————————')
        st.write('—————————————————————————————————————————————————')
        st.write(' ')
        st.write(':blue[出现，可以留意一下]')
        st.write(' ')
        st.write(':red[分界线已经泪目了]')
    st.write('————————————————————我也是有底线的————————————————————')
    st.write('—————————————————————————————————————————————————')


def page_6():
    st.title('_👏用过的人都说好！_')
    tab1,tab2,tab3,tab4,tab5 = st.tabs(['聪明的计算机','我会取名字！','不要点我！','猜身份','传送门'])
    with tab1:
        nums = st.text_input('请输入算式：')
        if nums:
            nl = [1,2,3]
            n = choice(nl)
            if n == 1:
                st.write(':red[我不会，长大后再来学吧]')
            elif n==2:
                st.write(':red[想偷懒？]')
            else:
                st.write(':red[（计算机跑路了）]')
    with tab2:
        father_name = None
        if not father_name:
            father_name = st.text_input('请输入父亲名字：')
        mother_name = None
        if not mother_name:
            mother_name = st.text_input('请输入母亲名字：')
        if father_name and mother_name:
            st.write('你们孩子的名字是：')
            st.subheader(father_name[0]+mother_name[0]+"!")
    with tab3:
        i = 0
        u = 0
        bar_num = 0
        latest_iteration = st.empty()
        bar= st.progress(0,'__加载后免费送美味蛋糕！ awa__')
        t = st.button('点我加载')
        if t:
            for i in range(99):
                latest_iteration.text(f'{i+1}%')
                bar.progress(i + 1)
                sleep(0.1)
            st.write(':red[__蛋糕是个谎言！__]')
        st.write('----')
        st.write(' ')
        st.write('__多选题__')
        st.write(' ')
        st.write('__勾选正确选项(多选) 1+1=?__')
        col1,col2,col3,col4 = st.columns([1,1,1,1])
        col5,col6 = st.columns([3,2])
        with col1:
            cb1 = st.checkbox('3')
        with col2:
            cb2 = st.checkbox('钝角')
        with col3:
            cb3 = st.checkbox('刘邦')
        with col4:
            cb4 = st.checkbox('24')
        lb = [cb1,cb2,cb3,cb4]
        if st.button('提交'):
            u = 1
        if True in lb :
            if u == 1:
                st.write(':red[__错！有没有种可能啥也不选__]')
        else:
            if u == 1:
                with col5:
                    st.subheader(':green[__你撞对的吧？__]')
                with col6:
                    st.image('表情包.png')
        st.write('----')
        st.write('__问题在答案里__')
        col7,col8,col9,col10 = st.columns([1,1,1,2])
        col11,col12,col13,col14 = st.columns([1,1,1,2])
        col15,col16 = st.columns([3,2])
        with col7:
            cb7 = st.checkbox('两根须')
        with col8:
            cb8 = st.checkbox('五对脚')
        with col9:
            cb9 = st.checkbox('身体是弯的')
        with col10:
            cb10 = st.checkbox('这只虾的特点是？')
        with col11:
            cb11 = st.checkbox('有一双眼睛')
            cb15 = st.checkbox('是熟的')
        with col12:
            cb12 = st.checkbox('看着屏幕')
            cb16 = st.checkbox('熟的前一秒是活着的')
        with col13:
            cb13 = st.checkbox('坐着椅子')
            cb17 = st.checkbox('虾的头上有一行字')
        with col14:
            cb14 = st.image('虾.jpg')
        if st.button('提交答案'):
            i = 1
        li = [cb7,cb8,cb9,cb10,cb11,cb12,cb13,cb15,cb16,cb17]
        

        if False in li:
            if i == 1:
                st.write(':red[__错！少了！__]')
        else:
            if i == 1:
                with col15:
                    st.subheader(':green[__猜对的吧?__]')
                with col16:
                    st.image('表情包.png')

        st.write('----')
        st.write(' ')
        st.write('__综合题__')
        st.write(' ')
        que,shuzhou = st.columns([1,4])
        with que:
            st.write('__请在数轴上表示-2.4<x<4.2的整数解集__')
        with shuzhou:
            ber1,ber2 = st.slider('参考数轴：', -10, 10, (-1,1))
            st.write('解集：', ber1,'≤ x ≤',ber2)
        if st.button('是否提交?'):
            if ber1 == -2 and ber2 == 4 :
                st.write(':green[__很好，你发现了吗，上面的表达式里暗藏玄机__]')
            else:
                st.write(':red[__错了！__]')
        st.write('----')
        st.write(' ')
        st.write('__单选题__')
        st.write(' ')
        col17,col18 = st.columns([1,3])
        with col18:
            man = st.radio(
                '__上面那题的解集中的数字所组成的十位数的相反数是谁的号码？__',
                ['本网站作者', 'Kobe', '米老鼠','屏幕前的你！','coke']
            )
        with col17:
            st.write('__来道单选题！__')
            for j in range(4):
                st.write('_'*j+'awa')
        col19,col20 = st.columns([1,1])
        if man == 'Kobe':
            with col19:
                change_geshi(5)
                st.write(':green[__想到这，泪目了 qwq__]')
                change_geshi(5)
                with open('seeyouagain.mp3','rb') as f:
                    my_mp3 = f.read()
                st.audio(my_mp3,format = 'audio/mp3',start_time = 0)
            with col20:
                st.image('冰红茶.jpg')
                
        elif man == '本网站作者':
            st.write(':red[……]')
        else:
            st.write(':red[__不是，也可以错？__]')
        st.write('----')
        col21,col22 = st.columns([1,1])
        with col21:
            day = st.radio(
                '__2024年7月23日是什么日子？__',
                ['平常日', 'Kobe坠机日', '该网站发布日','肘击节','大暑','小暑','中暑'])
        with col22:
            st.write('__再来道单选题！__')
            for j in range(5,10):
                st.write('_'*j+'awa')
        if day == 'Kobe坠机日' or day == '肘击节':
            st.write(':red[__你觉得呢？  =)__]')
        elif day == '该网站发布日':
            st.write(':green[__你怎么知道？ awa__]')
        elif day == '平常日':
            st.write(':red[__对了！对了？  =)__]')
        elif day == '大暑' or day == '小暑':
            st.write(':red[__错了！__]')
        else:
            st.write(':red[__我看你是中暑了 =)__]')
        st.write('----')
                
    with tab4:
        job = st.text_input('请输入1—3条线索（写完再回车）：')
        if job:
            st.write(':red[我猜你是…………]')
            sleep(3)
            st.write(':red[生物！]')
            sleep(1)
            st.write(':red[得意ing……]')
    with tab5:
        st.subheader('你要去哪？')
        co1,co2,co3,co4 = st.columns([1,1,1,1])
        co5,co6,co7,co8 = st.columns([1,1,1,1])
        with co1:
            st.link_button('百度半下','https://www.baidu.com/')
        with co2:
            st.link_button('小破站', 'https://www.bilibili.com/')
        with co3:
            st.link_button('智慧教育','https://basic.smartedu.cn/')
        with co4:
            st.link_button('百度翻译','https://fanyi.baidu.com/mtpe-individual/multimodal#/')
        with co5:
            st.link_button('我的世界wiki','https://minecraft.fandom.com/zh/wiki/Minecraft_Wiki')
            
    st.write(' ')
    st.subheader(':blue[_👇评价一下！_]')
    c1,c2,c3,c4,c5 = st.columns([1,1,1,1,1])
    with c1:
        a1 = st.button('👍')
    with c2:
        a2 = st.button('好')
    with c3:
        a3 = st.button('好用')
    with c4:
        a4 = st.button('太好用了')
    with c5:
        a5 = st.button('这是我见过最好用的')
    if a1 or a2 or a3 or a4 or a5:
        st.write(':blue[_谢谢评价，祝您生活愉快！_]')
    
    
def change_img(img,rc,rb,rg):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][rg]
            b = img_array[x,y][rb]
            img_array[x,y] = (r,b,g)
    return img
def fan_img(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = 255- img_array[x,y][0]
            g = 255- img_array[x,y][1]
            b = 255- img_array[x,y][2]
            img_array[x,y] = (r,b,g)
    return img

# def xiang_img(img):
#     block=img.crop((0,0,10,10))

#     s=5
#     width=img.size[0]
#     height=img.size[1]
    
#     img_new=Image.new("RGB",img.size)
#     for y in range(0,height,s):
#         for x in range(0,width,s):
#             block=img.crop((x,y,x+s,y+s))
    
#             pixel_list=list(block.getdata())
#             most_colors=Counter(pixel_list).most_common(1)[0][0]
#             block_new=Image.new("RGB",block.size,most_colors)        
            
#             img_new.paste(block_new,(x,y))

#     return img_new
def daxiao_img(img):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][0]
            g = img_array[x,y][1]
            b = img_array[x,y][2]
            rgb= [r,g,b]
            r_n = max(r,g,b)
            g_n = min(r,g,b)
            b_n = r_n+g_n
            if b_n > 255:
                b_n -= 255
            img_array[x,y] = (r_n,b_n,g_n)
    return img

def change_geshi(hangshu):
    for i in range(hangshu):
        st.write(' ')

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的成分复杂的图鉴':
    page_5()
elif page == '好用小工具':
    page_6()
