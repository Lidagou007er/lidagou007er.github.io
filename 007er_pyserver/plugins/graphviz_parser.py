from graphviz import Digraph,render,pipe
class Graphiviz_Parser():

    #======= 关系文件处理模块   ==========
    def dot_to_svg(dot_str):
        return pipe('dot','svg',dot_str.encode()).decode('utf-8')
    '''dot转svg'''
    '''
    def save_dot_and_svg(filename,content):
        gv_file_w = open("app/relationships/" + filename, 'w')
        gv_file_w.write(content)
        print("the content is {0}".format(content))
        gv_file_w.close()
        render('dot', 'svg', "app/relationships/" + filename)
    '''

    '''读取dot文件'''
    '''
    def read_dot(filename):
        dot_file = open('app/relationships/' + filename, 'r')
        dot_content = ""
        for eachline in dot_file:
            dot_content = dot_content + eachline
        dot_file.close()
        return dot_content
    '''
    '''dot转svg并返回'''
    '''
    def read_svg(filename):
        svg_file = open("app/relationships/" + filename + '.svg', 'r')
        svg_content = ""
        for eachline in svg_file:
            svg_content= svg_content + eachline

        return svg_content
    '''
    #============= end ===============


    #========在svg文件里增加链接========
    def add_links(nodes,svg_text):
        for node in nodes:
            begin_pos=svg_text.find(str(node)+"<")-8
            print("aabbccd")
            print(begin_pos)
            #svg_text=svg_text[:begin_pos]+ \
                         #" onClick=alert_test()"+svg_text[begin_pos:]
            svg_text=svg_text[:begin_pos]+ \
                         " onmouseover=mouse_over_it(\'"+str(node)+"\')"+\
                     " onClick=change_it(\'"+str(node)+"\')"+svg_text[begin_pos:]
            print(svg_text)
        return svg_text
    #============= end ===============

    #===解析graphviz_python语言(不用)===
    def get_nodes(gvcontent):
        nodes=[]
        while(gvcontent.find("node")!=-1):

            #deal node
            begin_pos=gvcontent.find("node")+6
            end_pos=gvcontent[begin_pos:].find("\'")+begin_pos
            nodes.append(gvcontent[begin_pos:end_pos])
            gvcontent=gvcontent[end_pos:]

        print("nodes:")
        print(nodes)
        return nodes
    #==按照graph_python语言绘图(不用)===
    def draw_graph(gvcontent):
        print("nodes:")
        print("before trans:")
        print(gvcontent)

        h = Digraph('hello_svg', format='svg')

        exec(gvcontent)

        print("after trans:")

        svg_original=h.pipe().decode("utf-8")
        print(svg_original)

        nodes=Graphiviz_Parser.get_nodes(gvcontent)
        for node in nodes:
            begin_pos=svg_original.find(node+"<")-8
            print("aabbccd")
            print(begin_pos)
            #svg_original=svg_original[:begin_pos]+ \
                         #" onClick=alert_test()"+svg_original[begin_pos:]
            svg_original=svg_original[:begin_pos]+ \
                         " onClick=change_it(\'"+node+"\')"+svg_original[begin_pos:]
            print(svg_original)
        return svg_original

    #==   解析指定格式文本 ===
    def analysis_text(gv_id,the_text):

        # text_example：
        '''
        ^^A TITLEA
        this is a line.
        ^^B TITLEB
        this is the second line.
        ^^C TITLEC
        第三行
        '''

        ids = []
        id_and_conceptions = {}
        id_and_paragraphs = {}
        while the_text.find("^^") != -1:
            id_begin = the_text.find("^^") + 2
            id_end = the_text.find(" ")

            #文章id+节点名称生成唯一标识码
            id = str(gv_id)+the_text[id_begin:id_end]
            the_text = the_text[id_end + 1:]

            conception_end = the_text.find("\n")
            conception = the_text[:conception_end]

            id_and_conceptions[id] = conception

            the_text = the_text[conception_end + 1:]
            paragraph_end = the_text.find("^^")
            paragraph = the_text[:paragraph_end]

            id_and_paragraphs[id] = paragraph
            the_text = the_text[paragraph_end:]
            ids.append(id)

        print(id_and_conceptions)
        print(id_and_paragraphs)

        return [ids, id_and_conceptions, id_and_paragraphs]

    #解析后的文本text_to_graphviz
    def text_to_graphviz(ids_conceptions_paragraphs):
        ids = ids_conceptions_paragraphs[0]
        id_and_conceptions = ids_conceptions_paragraphs[1]
        id_and_paragraphs = ids_conceptions_paragraphs[2]
        h = Digraph('hello_svg', format='svg')
        for index, id in enumerate(ids):
            # 添加节点
            h.node(id, id_and_conceptions[id])

            if index < len(ids) - 1:
                print(index, len(ids))
                h.edge(id, ids[index + 1])
        svg_original=h.pipe().decode("utf-8")
        svg_add_links=Graphiviz_Parser.add_links(ids,svg_original)
        return svg_add_links





