class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # Step 1: Sort the folders
        folder.sort()

        # Step 2: Create a result list
        result = []
        prev = ""

        # Step 3: Loop through each folder in the sorted list
        for curr in folder:
            if not prev or not curr.startswith(prev + "/"):
                result.append(curr)
                prev = curr

        # Step 4: Return the result
        return result