#include <iostream>
#include <vector>
#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
	int m = nums1.size(), n = nums2.size();
	if (m < n) return findMedianSortedArrays(nums2, nums1);
	if (n == 0) return ((double)nums1[(m - 1) / 2] + (double)nums1[m / 2]) / 2.0;
	int left = 0, right = n * 2;

	while (left <= right) {
	    int mid2 = (left + right) / 2;
	    int mid1 = m + n - mid2;
	    double L1 = mid1 == 0 ? INT_MIN : nums1[(mid1 - 1) / 2];
	    double L2 = mid2 == 0 ? INT_MIN : nums2[(mid2 - 1) / 2];
	    double R1 = mid1 == m * 2 ? INT_MAX : nums1[mid1 / 2];
	    double R2 = mid2 == n * 2 ? INT_MAX : nums2[mid2 / 2];
	    if (L1 > R2) left = mid2 + 1;
	    else if (L2 > R1) right = mid2 - 1;
	    else return (max(L1, L2) + min(R1, R2)) / 2;
	}
	return -1;
}

int main() {
	int A[7] = {8,9,10,11,12,13,14};
	int B[12] = {1,2,3,4,21,22,23,24,25,26,27,34};
	vector<int> a(A,A+7);
	vector<int> b(B,B+12);
	cout << "the median of the two sorted arrays is : " 
		<< findMedianSortedArrays(a,b)
		<< endl;
	return 0;
}
