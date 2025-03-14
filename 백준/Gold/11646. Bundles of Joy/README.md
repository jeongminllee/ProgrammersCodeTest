# [Gold II] Bundles of Joy - 11646 

[문제 링크](https://www.acmicpc.net/problem/11646) 

### 성능 요약

메모리: 111940 KB, 시간: 152 ms

### 분류

비트 집합, 다이나믹 프로그래밍

### 제출 일자

2025년 1월 26일 20:51:37

### 문제 설명

<p>Bob’s Bakery is celebrating its grand opening! To commemorate this exciting occasion, they are offering a “Bundles of Joy” sale to encourage people to sample their full range of delectable desserts.</p>

<p>For example, you can buy the “Chocolate Cakes” bundle which includes chocolate layer cake and black forest cake for <span>$</span>20. Or you can buy the “Fruity Cakes” bundle which includes lemon pound cake and key lime cake, also for <span>$</span>20. They offer an even bigger bundle that includes a slice of each of these cakes for an even lower price of <span>$</span>38.</p>

<p>You want to try out each dessert they offer. So, you need to buy some bundles to ensure you get at least one of each dessert. Of course, your goal is to do this while minimizing the amount of money you spend on bundles.</p>

<p>Finally, you make a few observations about the bundles they offer:</p>

<ul>
	<li>For any two bundles A and B, either every dessert in A is also in B, every dessert in B is also in A, or there is no dessert in both A and B.</li>
	<li>The only way to buy an item individually is if it is in a bundle of size 1. Not all items are in such a bundle.</li>
	<li>The pricing is not very well thought out. It may be cheaper to acquire items in a bundle B by buying some combination of other bundles rather than B itself.</li>
</ul>

### 입력 

 <p>The first line contains a single integer T ≤ 50 indicating the number of test cases. The first line of each test case contains two integers n and m where n is the number of different types of desserts offered by Bob’s Bakery and m is the number of different bundles. Here, 1 ≤ n ≤ 100 and 1 ≤ m ≤ 150.</p>

<p>Then m lines follow, each describing a bundle. The ith such line begins with two positive integers p<sub>i</sub> and s<sub>i</sub>. Here, 0 < p<sub>i</sub> ≤ 10<sup>6</sup> is the price of bundle i and 1 ≤ s<sub>i</sub> ≤ n is the number of items in bundle i. The rest of this line consists of si distinct integers ranging from 1 to n, indicating what desserts are included in this bundle.</p>

<p>Each of the n items will appear in at least one bundle.</p>

### 출력 

 <p>The output for each test case is a single line containing the minimum cost of purchasing bundles to ensure you get at least one of each item. This value is guaranteed to fit in a 32-bit signed integer.</p>

