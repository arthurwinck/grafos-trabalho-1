flag_num_vertices = False
        flag_get_vertices = False
        flag_get_vertices_rotulo = False
        lista_vertices_index = []
        lista_vertices_rotulo = []

        for linha in linhas:
            for palavra in linha:
                if palavra == '*vertices':
                    flag_num_vertices = True

                if palavra == '*edges':
                    flag_num_vertices = False
                    flag_get_vertices = False
                    flag_get_arestas = True

                if flag_num_vertices:
                    num_vertices = palavra
                    flag_num_vertices = False
                    flag_get_vertices = True

                if flag_get_vertices_rotulo:
                    lista_vertices_rotulo.append(palavra)
                    flag_get_vertices_rotulo = False

                if flag_get_vertices:
                    flag_get_vertices_rotulo = True
                    lista_vertices_index.append(palavra)

                if flag_get_arestas:

        return None