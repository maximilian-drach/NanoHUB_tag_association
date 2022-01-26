#!/usr/bin/env python3
import tag_analysis as ta
import argparse


def main():
    parser = argparse.ArgumentParser(description='A script that returns a tsv file of the frequency of all the tags associated with a tag')
    parser.add_argument('-tdf', '-tags', type=str, default='tags.tsv', dest='tagsDF', help='Specify the tags.tsv file (the file with all the tags number and names)')
    parser.add_argument('-todf', '-tags_obj', type=str, default='tags_obj.tsv', dest='tags_objDF', help='Specify the tags_obj.tsv file (the file with all courses, resources, etc)')
    parser.add_argument('-t', '-tag_name', dest='tag', nargs='?', type=str,  help='Put this at the end of the script and type the tag name.')
    parser.add_argument('-o', '-o', dest='output', type=str, help='Type the outputs path for the tsv file')

    #change to path based for the tag.tsv and tag_obj. take the path
    #no trailing slash!!!!!
    results = parser.parse_args()
    
    if results.tag is None:
        raise ValueError("!!Please enter a tag name!!")

    key = results.tag.replace(" ",'').lower()
    if results.output is None:
        ta.tag_association_tsv_print(results.tags_objDF, results.tagsDF, key)
    else:
        ta.tag_association_tsv(results.tags_objDF, results.tagsDF, key, results.output)


if __name__ == '__main__':
    main()