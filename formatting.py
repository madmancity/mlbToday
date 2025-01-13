
from datetime import datetime
def format_name(plrname):
    last = plrname.split()[-1];
    if("Jr" in last):
        last = plrname.split()[-2]
    initials = "".join(filter(str.isupper, plrname))
    return initials[0] + ". " + last[:7];


def getdate():
    y_cur = str(datetime.now().year);
    m_cur = str(datetime.now().month);
    d_cur = str(datetime.now().day);
    if(len(m_cur) == 1):
        m_cur = '0'+m_cur;
    if(len(d_cur) == 1):
        d_cur = '0'+d_cur;
    return y_cur+"-"+m_cur+"-"+d_cur;

def utctoest(time):
    tlist = time.split(":");
    if int(tlist[0]) > 12:
        tlist[0] = str(int(tlist[0])-5);
    else:
        tlist[0] = str(int(tlist[0])-5)
    newtime = tlist[0] + ":" + tlist[1];
    return newtime

