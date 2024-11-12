import streamlit as st
from longest_palindrome import Solution

def main():
    st.title("Longest Palindrome Finder")

    st.write("Enter a string to find the longest palindrome substring.")

    input_string = st.text_input("Input String")

    if st.button("Find Longest Palindrome"):
        if input_string:
            solution = Solution()
            result = solution.longestPalindrome(input_string)
            st.write(f"Longest palindrome: {result}")
        else:
            st.write("Please enter a string.")

if __name__ == "__main__":
    main()
