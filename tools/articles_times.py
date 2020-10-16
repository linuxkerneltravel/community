#!/usr/bin/env python3

import glob
import frontmatter


list=[]

def main():
    files = glob.glob('*/index.md')
    #删除index.md
    # if files:
    #     files.remove('index.md')
    for f in files:
        get_author(f)
    count_num(list)
    format_print(count_num(list))


def get_author(md_file):    
    md = frontmatter.load(md_file)
    list.append(md.get('author'))


def count_num(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result

def format_print(author_list):
    author_list=sorted(author_list.items(),key=lambda d:d[1],reverse=True) #按值来排序 如果是False 则为正序
    # print(author_list)
    print("  文章数         作者  ")
    print("=========================")
    for index, val in enumerate(author_list):
       print(" ",'{:<8}\t -'.format(val[1]),val[0])



if __name__ == '__main__':
    main()



