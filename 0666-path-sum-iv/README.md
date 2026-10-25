<h2><a href="https://leetcode.com/problems/path-sum-iv">666. Path Sum IV</a></h2><h3>Medium</h3><hr><p>If the depth of a tree is smaller than <code>5</code>, then this tree can be represented by an array of three-digit integers. You are given an <strong>ascending </strong>array <code>nums</code> consisting of three-digit integers representing a binary tree with a depth smaller than <code>5</code>, where for each integer:</p>

<ul>
	<li>The hundreds digit represents the depth <code>d</code> of this node, where <code>1 &lt;= d &lt;= 4</code>.</li>
	<li>The tens digit represents the position <code>p</code> of this node within its level, where <code>1 &lt;= p &lt;= 8</code>, corresponding to its position in a <strong>full binary tree</strong>.</li>
	<li>The units digit represents the value <code>v</code> of this node, where <code>0 &lt;= v &lt;= 9</code>.</li>
</ul>

<p>Return the <strong>sum</strong> of <strong>all paths</strong> from the <strong>root</strong> towards the <strong>leaves</strong>.</p>

<p>It is <strong>guaranteed</strong> that the given array represents a valid connected binary tree.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/30/pathsum4-1-tree.jpg" style="width: 212px; height: 183px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [113,215,221]</span></p>

<p><strong>Output:</strong> <span class="example-io">12</span></p>

<p><strong>Explanation:</strong></p>

<p>The tree that the list represents is shown.<br />
The path sum is (3 + 5) + (3 + 1) = 12.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/30/pathsum4-2-tree.jpg" style="width: 132px; height: 183px;" /></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [113,221]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>The tree that the list represents is shown.&nbsp;<br />
The path sum is (3 + 1) = 4.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 15</code></li>
	<li><code>110 &lt;= nums[i] &lt;= 489</code></li>
	<li><code>nums</code> represents a valid binary tree with depth less than <code>5</code>.</li>
	<li><code>nums</code> is sorted in ascending order.</li>
</ul>
