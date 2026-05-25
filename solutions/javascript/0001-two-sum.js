/**
 * Problem: Two Sum
 * Link: https://leetcode.com/problems/two-sum/
 * Difficulty: Easy
 * Topics: Array, Hash Table
 * Time: O(n)
 * Space: O(n)
 *
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const seen = new Map();

  for (let index = 0; index < nums.length; index += 1) {
    const complement = target - nums[index];
    if (seen.has(complement)) {
      return [seen.get(complement), index];
    }
    seen.set(nums[index], index);
  }

  return [];
};
