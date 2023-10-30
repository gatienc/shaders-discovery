''' Read shader source from file. '''


def read_shader_source(file_path):
    '''
    Read shader source from file.
    --- Parameters ---
    file_path: str
        Path to shader source file.
    --- Returns ---
    shader_source: str
    '''
    with open(file_path, 'r', encoding='utf-8') as shader_file:
        shader_source = shader_file.read()
    return shader_source
