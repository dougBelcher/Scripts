# ???
def download(url, stream=None):
    print(f'Downloading {url}', file=stream)
    #...
import io
memory_buffer = io.StringIO()
download('app.js', memory_buffer)
download('style.css', memory_buffer)
memory_buffer.getvalue()
