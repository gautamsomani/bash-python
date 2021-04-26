#!/usr/bin/env python3
#

import re
import argparse
import sys

class check_disk_io:



#    if len(sys.argv) < 7:
#        print('Too few arguments.')
#        sys.exit()


    
    def get_partitions(self):

        DISK=[]

        with open('/proc/partitions') as officialData:
            lines=[]
            for line in officialData:
                lines.append(line)
        
        ignoreRegex=re.compile('md.*$|major|^$|\d$')

        for line in lines:
            if ignoreRegex.search(line) is None:
                DISK.append(line.split()[3])
    
        return DISK



    def parse_arguments(self):
    
        parser = argparse.ArgumentParser(description="Check the disk I/O's in kb/s across all physical disks.",
                            epilog="systat only gives in average, hence this script")
    
        parser.add_argument("-w", metavar="WARN_READ", help="WARN_READ", type=int, required=True)
        parser.add_argument("-c", metavar="CRITICAL_READ", help="CRITICAL_READ", type=int)
        parser.add_argument("-e", metavar="WARN_WRITE", help="WARN_WRITE", type=int, required=True)
        parser.add_argument("-v", metavar="CRITICAL_WRITE", help="CRITICAL_WRITE", type=int)
        #parser.add_argument("-h")
        parser.add_argument("-p")
    
        args = parser.parse_args()
    
        if args.w: 
            RWARN = args.w
        if args.c:
            RCRIT = args.c
        if args.e:
            WWARN = args.e
        if args.v:
            WCRIT = args.v
        if args.p:
            PERF = 1
    
        #print("{0}, {1}, {2}, {3}".format(RWARN, RCRIT, WWARN, WCRIT))
        #return




    def status(self):

        if READS < RWARN:
            MSG = "read kb/s normal"
            EXIT = 0
            STATUS = "OK"
        elif READS < RCRIT:
            MSG = "read kb/s anormal"
            EXIT = 1
            STATUS = "WARNING"
        else:
            MSG = "read kb/s critical"
            EXIT = 2
            STATUS = "CRITICAL"

        if WRITES < WWARN:
            MSG = MSG + "write kb/s normal"
            EXIT = 0
            STATUS = "OK"
        elif WRITES < WCRIT:
            MSG = MSG + "write kb/s anormal"
            EXIT = 1
            STATUS = "WARNING"
        else:
            MSG = MSG + "write kb/s critical"
            EXIT = 2
            STATUS = "CRITICAL"

        if PERF == 1:
            PERF="| writes={0};{1};{2} ;; reads={3};{4};{5} ;;".format(WRITES,WWARN,WCRIT,READS,RWARN,RCRIT)




    def output(self):

        print("{0} - {1} {2}".format(STATUS, MSG, PERF))



    def get_mb(self):

        DISKS=self.get_partitions()
        with open('/proc/diskstats') as diskStats:
            lines=[]
            for line in diskStats:
                lines.append(line)

        for DISK in DISKS:
            diskRegex = re.compile('(%s)'%DISK)
            print(type(diskRegex))
            #diskStat = diskRegex.search(lines)
            #print(diskStat.groups())
            


object = check_disk_io()
object.parse_arguments()
object.get_mb()
