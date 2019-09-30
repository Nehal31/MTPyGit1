
import datetime
import re


def get_time_regex(st, et):
    print(st)
    print(et)
    s_dt = datetime.datetime.strptime(st, "%a %b %d %H:%M:%S %Z %Y")
    e_dt = datetime.datetime.strptime(et, "%a %b %d %H:%M:%S %Z %Y")

    s_hour = s_dt.hour
    s_minutes = s_dt.minute
    s_seconds = s_dt.second
    s_date = s_dt.day

    e_hour = e_dt.hour
    e_minutes = e_dt.minute
    e_seconds = e_dt.second
    e_date = e_dt.day

    diff = e_dt - s_dt
    print("In Seconds %d " % diff.seconds)
    sec = diff.seconds
    if not sec // 60:
        if (sec % 60) < 10:
            start_place = int(("%02d" % s_seconds)[1])
            end_place = int(("%02d" % e_seconds)[1])
            if start_place == end_place:
                regex = r"%02d %02d:%02d:%02d" % (s_date, s_hour, s_minutes, s_seconds)
            elif start_place < end_place:
                s_seconds = int(("%02d" % s_seconds)[0])
                regex = r"%02d %02d:%02d:%d[%d-%d]" % (s_date, s_hour, s_minutes, s_seconds, start_place, end_place)
            elif start_place > end_place:
                dec_start_place = int(("%02d" % s_seconds)[0])
                dec_end_place = dec_start_place + 1
                regex = r"%02d %02d:%02d:(%d[%d-%d]|%d[%d-%d])" % (s_date, s_hour, s_minutes,
                                                                dec_start_place, start_place, 9,
                                                                dec_end_place, 0, end_place, )
                print(regex)

        elif(sec % 60) >= 10:
            start_place = int(("%02d" % s_seconds)[0])
            end_place = int(("%02d" % e_seconds)[0])
            if start_place < end_place:
                regex = r"%02d %02d:%02d:[%d-%d]\d" % (s_date, s_hour, s_minutes, start_place, end_place)
            else:
                m_start_place = int(("%02d" % s_minutes)[1])
                m_end_place = m_start_place + 1 if m_start_place < 9 else 0
                s_minutes = int(("%02d" % s_minutes)[0])
                regex = r"%02d %02d:%d(%d:[%d-%d]|%d:[%d-%d])\d" % (s_date, s_hour, s_minutes,
                                                                    m_start_place, start_place, 5,
                                                                    m_end_place, 0, end_place)
            print(regex)

    elif not sec // (60 * 60):
        sec = sec // 60
        if sec % 60 < 10:
            start_place = int(("%02d" % s_minutes)[1])
            end_place = int(("%02d" % e_minutes)[1])
            if start_place < end_place:
                s_minutes = int(("%02d" % s_minutes)[0])
                regex = r"%02d %02d:%d[%d-%d]:[0-5]\d" % (s_date, s_hour, s_minutes,
                                                   start_place, end_place)
            elif start_place > end_place:
                dec_start_place = int(("%02d" % s_minutes)[0])
                dec_end_place = dec_start_place + 1
                regex = r"%02d %02d:(%d[%d-%d]|%d[%d-%d]):[0-5]\d" % (s_date, s_hour,
                                                                        dec_start_place, start_place, 9,
                                                                        dec_end_place, 0, end_place, )
            print(regex)
        elif sec % 60 >= 10:
            start_place = int(("%02d" % s_minutes)[0])
            end_place = int(("%02d" % e_minutes)[0])
            if start_place < end_place:
                regex = r"%02d %02d:[%d-%d]\d:[0-5]\d" % (s_date, s_hour, start_place, end_place)
            else:
                m_start_place = int(("%02d" % s_hour)[1])
                m_end_place = m_start_place + 1
                s_hour = int(("%02d" % s_hour)[0])
                regex = r"%02d %d(%d:[%d-%d]|%d:[%d-%d])\d:[0-5]\d" % (s_date, s_hour,
                                                                        m_start_place, start_place, 5,
                                                                        m_end_place, 0, end_place)
            print(regex)


    elif not sec // (60 * 60 * 60):
        sec = sec // (60 * 60)
        if sec % 60 < 10:
            start_place = int(("%02d" % s_hour)[1])
            end_place = int(("%02d" % e_hour)[1])
            if start_place < end_place:
                s_hour = int(("%02d" % s_hour)[0])
                regex = r"%02d %d[%d-%d]:[0-5]\d:[0-5]\d" % (s_date, s_hour,
                                                            start_place, end_place)
            elif start_place > end_place:
                dec_start_place = int(("%02d" % s_hour)[0])
                dec_end_place = dec_start_place + 1 if dec_start_place < 9 else 0
                regex = r"%02d (%d[%d-%d]|%d[%d-%d]):[0-5]\d:[0-5]\d" % (s_date,
                                                                         dec_start_place, start_place, 9,
                                                                         dec_end_place, 0, end_place)

            print(regex)

        elif sec % 60 >= 10:
            start_place = int(("%02d" % s_hour)[0])
            end_place = int(("%02d" % e_hour)[0])
            if start_place < end_place:
                regex = r"%02d [%d-%d]\d:[0-5]\d:[0-5]\d" % (s_date, start_place, end_place)
            else:
                m_start_place = int(("%02d" % s_date)[1])
                m_end_place = m_start_place + 1 if m_start_place < 9 else 0
                s_date = int(("%02d" % s_date)[0])
                regex = r"%d(%d:[%d-%d]|%d:[%d-%d])\d:[0-5]\d:[0-5]\d" % (s_date,
                                                                          m_start_place, start_place, 5,
                                                                          m_end_place, 0, end_place)
    elif diff.days:
        print("Date Operation are not supported")
        return None


    def clean(reg):
        findings = re.findall(r'\[\d-\d\]', reg)
        for find in findings:
            str = re.sub(r"[\[\]]", "", find)
            n1, n2 = map(int, str.split('-'))
            if n1 == n2:
                np = "%d" % n1
            elif n1 + 1 == n2:
                np = "[%d%d]" % (n1, n2)
            else:
                np = "[%d-%d]" % (n1, n2)
            reg = reg.replace(find, np, 1)
        return reg


    regex = clean(regex)
    print(regex)

    return regex



def test():
    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 27 09:13:41 UTC 2019'

    get_time_regex(s_date, e_date) # Fri Sep 27 09:13:(39|4[01]) UTC 2019

    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 28 09:13:51 UTC 2019'

    get_time_regex(s_date, e_date) # Fri Sep 27 09:13:(39|4\d|51) UTC 2019

    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 28 09:14:29 UTC 2019'

    get_time_regex(s_date, e_date)  # Fri Sep 27 09:1(3:(39|[45]\d)|4:[0-2]\d) UTC 2019

    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 28 09:15:29 UTC 2019'

    get_time_regex(s_date, e_date)  # Fri Sep 27 09:1(3:(39|[45]\d)|4:[0-5]\d|5:[0-2]\d) UTC 2019

    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 28 09:35:29 UTC 2019'

    get_time_regex(s_date, e_date)  # Fri Sep 27 09:1(3:(39|[45]\d)|4:[0-5]\d|5:[0-2]\d)|2\d:[0-5]\d|3([0-4]:[0-5]\d|33:(39|[45]\d)|4:[0-5]\d|5:[0-2]\d) UTC 2019



if __name__ == '__main__':
    test()