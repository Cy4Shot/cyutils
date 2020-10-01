import subprocess, os, sys, platform
from tempfile import TemporaryDirectory
from cyutils.io import custom_error as ce 

def message_box(title, content, args=''):
    """Creats a message box. WINDOWS USERS ONLY!

    Parameters:
    title (string): Title of the message box.
    content (string): Content of the message box.
    args (string): VB arguments for message box (DEFAULT = '').
    """
    if platform.system() == 'Windows':
        with TemporaryDirectory() as temp_dir:
            with open(temp_dir + '\\data.vbs', 'w') as f:
                f.write('x=MsgBox("' + content + '", ' + args + ', "' + title + '")')
            subprocess.call('wscript //nologo ' + temp_dir + '\\data.vbs', stdout=open(os.devnull, 'w'), stderr=subprocess.STDOUT)
    else:
        ce.CustomError('OSError').throw("message_box is only available for Windows Users.")