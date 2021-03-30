from wordpress_xmlrpc import Client
from wordpress_xmlrpc.methods import posts
from wordpress_xmlrpc import WordPressPost


def CreatePost(title, content):
    my_blog = Client('http://janny.pe.kr/xmlrpc.php', 'wndhks92', 'TKFKDGO1018!')
    myposts=my_blog.call(posts.GetPosts())

    post = WordPressPost()
    post.title = title // 글 제목.
    post.slug='test'
    post.content = content // 글 내용.
    post.terms_names = {
                        'category': ["카테고리"] // 글을 포함시키고 싶은 카테고리를 넣으면된다.
    }
    post.id = my_blog.call(posts.NewPost(post))
    post.post_status = 'publish'
    my_blog.call(posts.EditPost(post.id, post))


CreatePost("제목", "내용")