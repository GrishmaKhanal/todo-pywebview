import os
import webview

def get_index_path():
    html_path = os.path.join(os.path.dirname(__file__), 'frontend', 'index.html')
    
    if not os.path.isfile(html_path):
        return "<HTML><BODY>NO HTML FILE FOUND</BODY></HTML>" 
    
    file_url = 'file://' + os.path.abspath(html_path)
    return file_url

def get_index_window(note_app):
    index_path = get_index_path()
    if index_path.startswith("file://"):
        print("file path")
        webview.create_window("Note Keeping App", index_path, js_api=note_app)
    else:
        print("no file")
        webview.create_window("Note Keeping App", html=index_path)
