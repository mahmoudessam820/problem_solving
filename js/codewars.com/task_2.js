/*

 *  Isograms

 *  An isogram is a word that has no repeating letters, 
 *  consecutive or non-consecutive. 

 *  Implement a function that determines whether a string that 
 *  contains only letters is an isogram. Assume the empty string is an isogram.

 *  Ignore letter case.

 *  Examples:

 *  "Dermatoglyphics" --> true
 *  "aba" --> false
 *  "moOse" --> false (ignore letter case)
 * 
 * Task URL: https://www.codewars.com/kata/isograms/train/javascript

*/

function isIsogram(str) {
    return str.toLowerCase().split('').filter((item, index, array) =>
        array.indexOf(item) === index).length === str.length;
}


