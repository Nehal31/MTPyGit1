
import datetime
import re




def number_regex2(a, b):
    """

    :param a: start number
    :param b: end number
    :return: string pattern covers all numbers within a and b
    """
    if a > b:
        return ""

    diff = b - a
    num1 = "%02d" % a
    num2 = "%02d" % b
    if num1 == num2:
        return num1

    reg = ""
    ln = len(num1) - 1
    if diff < 10:
        if num1[ln] < num2[ln]:
            reg = "%s[%s-%s]" % (num1[ln - 1], num1[ln], num2[ln])
        else:
            reg = "(%s[%s-%d]|%d[%d-%s])" % (num1[ln - 1], num1[ln],
                                             9, int(num1[ln - 1]) + 1,
                                             0, num2[ln])
    elif 10 <= diff < 60:
        n1_once = int(num1[ln])
        n2_once = int(num2[ln])

        n1_dec = int(num1[ln - 1])
        n2_dec = int(num2[ln - 1])

        if int(num1[ln - 1:]) < int(num2[ln - 1:]):
            first = "%d[%d-%d]" % (n1_dec, n1_once, 9)
            last = "%d[%d-%d]" % (n2_dec, 0, n2_once)
            if n2_dec - n1_dec >= 2:
                mid = "[%d-%d]\d" % (n1_dec + 1, n2_dec - 1)
                reg = "(%s|%s|%s)" % (first, mid, last)
            else:
                reg = "(%s|%s)" % (first, last)
    else:
        print("Invalid Entry...")
    print("Input a : %s \t b : %s Pattern ::::: %s " % (num1, num2, reg))
    return reg

def get_time_regex(st, et):
    print(st)
    print(et)
    s_dt = datetime.datetime.strptime(st, "%a %b %d %H:%M:%S %Z %Y")
    e_dt = datetime.datetime.strptime(et, "%a %b %d %H:%M:%S %Z %Y")

    s_hour = s_dt.hour
    s_minutes = s_dt.minute
    s_seconds = s_dt.second
    s_date = s_dt.day
    s_month = s_dt.strftime("%b")
    print(s_month)

    e_hour = e_dt.hour
    e_minutes = e_dt.minute
    e_seconds = e_dt.second
    e_date = e_dt.day
    e_month = e_dt.strftime("%b")
    print(s_month)

    diff = e_dt - s_dt
    print("In Seconds %d " % diff.seconds)
    sec = diff.seconds

    if diff.days:
        return

    elif not sec // 60:
        if s_seconds == e_seconds:
            regex = r"%02d %02d:%02d:%02d" % (s_date, s_hour, s_minutes, s_seconds)
        elif s_seconds < e_seconds:
            reg_seconds = number_regex(s_seconds, e_seconds)
            regex = r"%s %02d %02d:%02d:%s" % (s_month, s_date, s_hour,
                                               s_minutes, reg_seconds)
        else:
            first_sec = "%s" % number_regex(s_seconds, 59)
            last_sec = "%s" % number_regex(0, e_seconds)

            if s_minutes < e_minutes:
                temp_regex = "(%02d:%s|%02d:%s)" % (s_minutes, first_sec, e_minutes, last_sec)
                regex = r"%s %02d %02d:%s" % (s_month, s_date, s_hour, temp_regex)
            else:
                if s_hour < e_hour:
                    temp_regex = "(%02d:%02d:%s|%02d:%02d:%s)" % (s_hour, s_minutes, first_sec,
                                                               e_hour, e_minutes, last_sec)
                    regex = r"%s %02d %s" % (s_month, s_date, temp_regex)
                else:
                    temp1 = "%02d %02d:%02d:%s" % (s_date, s_hour, s_minutes, first_sec)
                    temp2 = "%02d %02d:%02d:%s" % (e_date, e_hour, e_minutes, last_sec)
                    if s_date < e_date:
                        temp_regex = "(%s|%s)" % (temp1, temp2)
                        regex = r"%s %s" % (s_month, temp_regex)
                    else:
                        temp_regex = "(%s %s|%s %s)" % (s_month, temp1, e_month, temp2)
                        regex = r"%s" % temp_regex

    elif not sec // (60 * 60):
        if s_minutes == e_minutes:
            print("Error*****")
        first_sec = "%s" % number_regex(s_seconds, 59)
        last_sec = "%s" % number_regex(0, e_seconds)
        first_min = "%02d:%s" % (s_minutes, first_sec)
        last_min = "%02d:%s" % (e_minutes, last_sec)

        if s_minutes < e_minutes:
            if e_minutes - s_minutes >= 2:
                mid_min = "%s:[0-5]\d" % (number_regex(s_minutes + 1, e_minutes - 1))
                temp_regex = "(%s|%s|%s)" % (first_min, mid_min, last_min)
            else:
                temp_regex = "(%s|%s)" % (first_min, last_min)

            regex = r"%s %02d %02d:%s" % (s_month, s_date, s_hour, temp_regex)
        else:
            res = number_regex(s_minutes+1, 59)
            if res:
                mid_min = "%s:[0-5]\d" % res
                temp1_regex = "%02d:(%s|%s)" % (s_hour, first_min, mid_min)
            else:
                temp1_regex = "%02d:%s" % (s_hour, first_min)

            res = number_regex(0, e_minutes-1)
            if res:
                mid_min = "%s:[0-5]\d" % res
                temp2_regex = "%02d:(%s|%s)" % (e_hour, mid_min, last_min)
            else:
                temp2_regex = "%02d:%s" % (e_hour, last_min)

            if s_hour < e_hour:
                regex = r"%s %02d (%s|%s)" % (s_month, s_date, temp1_regex, temp2_regex)
            else:
                temp1 = "%02d %s" % (s_date, temp1_regex)
                temp2 = "%02d %s" % (e_date, temp2_regex)
                if s_date < e_date:
                    temp_regex = "(%s|%s)" % (temp1, temp2)
                    regex = r"%s %s" % (s_month, temp_regex)
                else:
                    temp_regex = "(%s %s|%s %s)" % (s_month, temp1, e_month, temp2)
                    regex = r"%s" % temp_regex



    elif not sec // (60 * 60 * 60):
        print("Not Supported Yet!!!")

    def clean(reg):
        print("Reg : %s" % reg)
        change = True
        counter = 0
        raw_reg = reg
        new_reg = reg
        while change:
            print("Counter ", counter)
            findings = re.findall(r'\[\d-\d\]', raw_reg)
            temp_reg = raw_reg
            for find in findings:
                str = re.sub(r"[\[\]]", "", find)
                n1, n2 = map(int, str.split('-'))
                if n1 == n2:
                    np = "%d" % n1
                elif n1 + 1 == n2:
                    np = "[%d%d]" % (n1, n2)
                elif n1 == 0 and n2 == 9:
                    np = "\d"
                else:
                    np = find
                temp_reg = temp_reg.replace(find, np, 1)

            findings = re.findall(r'(\d\\d\|(\d\\d\|?)+)', temp_reg)
            for find in findings:
                find = find[0]
                find = re.sub('^\D+', '', find)
                find = re.sub('\D+$', '', find)
                s, e = find[0], find[-1]
                np = "[%s-%s]" % (s, e)
                temp_reg = temp_reg.replace(find, np, 1)

            findings = re.findall(r'(\[\d-\d\]\\d\|(\d\\d\|?)+)', temp_reg)
            for find in findings:
                find = find[0]
                find = re.sub('^\D+', '', find)
                find = re.sub('\D+$', '', find)
                s, m, e = find[0], find[2], find[-1]
                if int(m) + 1 == int(e):
                    np = "%s-%s]" % (s, e)
                temp_reg = temp_reg.replace(find, np, 1)

            if temp_reg != raw_reg:
                raw_reg = temp_reg
                counter += 1
                continue

            change = False
            new_reg = raw_reg
        return new_reg

    regex = clean(regex)
    print(regex)

    return regex



def test():
    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 27 09:13:41 UTC 2019'
    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))


    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 27 10:12:51 UTC 2019'
    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))


    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 27 09:14:26 UTC 2019'
    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))


    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 27 09:15:26 UTC 2019'

    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))

    s_date = 'Fri Sep 27 09:49:39 UTC 2019'
    e_date = 'Fri Sep 27 09:50:26 UTC 2019'

    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))


    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 27 09:35:29 UTC 2019'

    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))


    s_date = 'Fri Sep 27 08:13:39 UTC 2019'
    e_date = 'Fri Sep 27 09:05:29 UTC 2019'

    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))

    s_date = 'Fri Sep 27 09:13:39 UTC 2019'
    e_date = 'Fri Sep 27 10:05:29 UTC 2019'

    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, s_date))
    s_date = 'Fri Sep 27 09:13:38 UTC 2019'
    print(re.search(reg, s_date))
    s_date = 'Fri Sep 27 09:13:59 UTC 2019'
    print(re.search(reg, s_date))

    s_date = "Mon Sep 25 23:59:59 UTC 2019"
    e_date = "Mon Sep 26 00:00:27 UTC 2019"
    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, e_date))

    s_date = "Mon Sep 25 22:59:13 UTC 2019"
    e_date = "Mon Sep 25 23:00:27 UTC 2019"
    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, e_date))

    s_date = "Mon Sep 25 23:12:13 UTC 2019"
    e_date = "Mon Sep 26 00:10:27 UTC 2019"
    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, e_date))

    s_date = "Mon Sep 30 23:59:58 UTC 2019"
    e_date = "Mon Oct 01 00:11:58 UTC 2019"
    reg = get_time_regex(s_date, e_date)
    print(re.search(reg, e_date))

if __name__ == '__main__':
    test()