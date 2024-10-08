
def htmltag(tag:str,s:str,id:str|None=None,klass:str|None=None,href:str|None=None,other_attribute:dict|None=None):
    """# htmltag
    htmlタグを作成
    ```py
    htmltag(tag="div",klass="title",s="ろくろ")
    #>>>'<div  class = "title"  >ろくろ</div>'
    ```
    * tag:htmlタグ
    * s:タグに挟まれるテキスト
    * id:id
    * klass:class
    * href:リンク
    * other_attribute:{"attribute":"values"}
    """
    id_ = ""
    if id:
        id_ = 'id = "%s"' % id
    klass_ = ""
    if klass:
        klass_ = 'class = "%s"' % klass
    id_ += ' ' + klass_
    href_ = ''
    if href:
        href_ = 'href = "%s"' % href
    id_ += ' ' + href_
    other_attribute_ = ""
    if other_attribute:
        for i in other_attribute.items():
            other_attribute_ += '%s = "%s"' % (i[0],i[1])
    id_ += ' ' + other_attribute_
    tagset = "<%s %s>\n%s\n</%s>\n" %(tag,id_,s,tag)
    return tagset
