from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost


import Sqlite3Conn

class PyMon:  
    def __init__(self):
        
        self.sqlConn = Sqlite3Conn.SQL_CONNECT()
        
        self.user = self.sqlConn.SQL_UserSelect('USER')   

    def CreatePost(self,title, content, id , password,category):
        my_blog = Client('http://janny.pe.kr/xmlrpc.php', id, password)
        myposts=my_blog.call(posts.GetPosts())

        post = WordPressPost()
        post.title = title ## 글 제목.
        post.slug='StockTrade'
        post.content = content ## 글 내용.
        post.terms_names = {
                            'post_tag' : category,
                            'category': ["주식 자동매매 일지"] ## 글을 포함시키고 싶은 카테고리를 넣으면된다.
        }
        post.id = my_blog.call(posts.NewPost(post))
        post.post_status = 'publish'
        my_blog.call(posts.EditPost(post.id, post))
    

        

    def run(self): 
        
        content = ''

        category_text ='' 
        nowdate = self.sqlConn.nowdate
        title =nowdate + '일 자동 매매 내역'

        content = content + '안녕하세요 좌니입니다. \n\n ' + nowdate + '자동 매매내역  포스팅을 시작하겠습니다. \n\n 시작에 앞서 자동 매매인점 확인 부탁드리며,\n 추전이 아닌 매매 내역을 포스팅 하고 있습니다.'
        content = content + '\n\n 투자에 책임을 지지 않습니다. \n\n자동 프로그램 특성상 오류 및 모의투자가 진행 될 수 있습니다.\n\n'
        
        #TODO 매도 내역 있으면 일일 보고서 작성
        #--------------완료---------------
        result = self.sqlConn.SQL_ListReport('STOCKSHISTORY')           
        
        content = content + '-------------------------------매도내역-------------------------------\n'
        content = content + '\n <a href="https://coupa.ng/bUFNXM" target="_blank" referrerpolicy="unsafe-url"><img src="https://ads-partners.coupang.com/banners/464315?subId=&traceId=V0-301-969b06e95b87326d-I464315&w=728&h=90" alt=""></a>\n'


        for stock in result:
            
            content = content + '종목코드 : ' + stock[0] +'\n'    
            content = content + '종목명 : ' + stock[1] +'\n'    
              
            content = content + '매수일자 : ' + stock[3] +'\n'    
            content = content + '수익률 : ' + str(stock[4]) +'\n'    
            content = content + '조건 검색명 : 조건_' + stock[5][-4:]+'\n'    

            content = content + '\n\n\n'    
            category_text =  category_text + stock[1]+","
            
	
        
        #매도종목 나열                   
        #TODO STOCKITEM  트렁케이트 진행 
        # -----------완료 ------------
        
        ## 보유종목 및 등락율 확인 보고서
        content = content + '-------------------------------보유내역-------------------------------\n'
        content = content + '<script src="https://ads-partners.coupang.com/g.js"></script><script>new PartnersCoupang.G({"id":464279,"trackingCode":"AF5288293","subId":null,"template":"carousel","width":"680","height":"140"});</script> \n'
        result_buy = self.sqlConn.SQL_ListSeach('STOCKBUY') 
        for stock_buy in result_buy: 
            content = content + '종목코드 : ' + stock_buy[0] +'\n'    
            content = content + '종목명 : ' + stock_buy[1] +'\n'                
            content = content + '매수일자 : ' + stock_buy[3] +'\n' 
            content = content + '수익률 : ' + str(stock_buy[4]) +'\n' 
            content = content + '조건 검색명 : 조건_' + stock_buy[8][-4:] +'\n' 
            content = content + '보유일 : ' + str(stock_buy[9]) +'일 보유중\n' 
            content = content + '\n\n\n'  

            category_text =  category_text + stock_buy[1]+","
        
        #보유 종목 나열

        category_text =  category_text + '키움, 자동 매매 프로그램, 수익률'
        

        content = content + '\n ' 
        
        print(content)
        content = content + '---주식 공부 책 추천---\n'
        content = content + '<script src="https://ads-partners.coupang.com/g.js"></script><script>	new PartnersCoupang.G({"id":464343,"template":"carousel","trackingCode":"AF5288293","width":"680","height":"140"});</script>\n\n'

        content = content + '주식 투자 하는 여러분 모두 성투 하시고,\n \n제 블로그에는 주식 관련 개발 관련 글이 많이있습니다.\n \n한번씩 둘러보셔서 좋은 프로그램 만들기를 기원합니다.\n\n(이 포스트는 자동으로 매일 오후 7시에 작성 됩니다.)'
        #금일 매수 종목 나열
                                                                 
        pymon.CreatePost(title, content,self.user[1],self.user[3].upper(),category_text)
        print("실행 완료")
    
        


pymon = PyMon()
pymon.run()


