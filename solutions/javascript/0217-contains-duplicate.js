/**
 * Problem: Contains Duplicate
 * Link: https://leetcode.com/problems/contains-duplicate/
 * Difficulty: Easy
 * Topics: Array, Hash Table, Sorting
 * Time: O(n)
 * Space: O(n)
 *
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function (nums) {
  return new Set(nums).size !== nums.length;
};
