int palindrome(int arr[], int start, int end) {
   // base case
   if (start >= end) {
      return 1;
   }
   if (arr[start] == arr[end]) {
      return palindrome(arr, start + 1, end - 1);
   } else {
      return 0;
   }
   // Driver code
   int main() {
   int arr[] = { 1, 2, 0, 2, 1 };
   int n = sizeof(arr) / sizeof(arr[0]);
   if (palindrome(arr, 0, n - 1) == 1)
      printf("Yes, the array is Palindrome\n");
   else
      printf("No, the array is not Palindrome\n");
   return 0;
}