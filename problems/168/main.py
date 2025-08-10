class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
            Este problema lo resolvi pensando que estoy en base 26 debido a que tengo 26 digitos con los cuales trabajar 1-26
        """
        column_name = ""
        while True:
            division = columnNumber // 26
            residuo = columnNumber % 26
            if residuo:
                column_name = chr(residuo + 64) + column_name
            elif division:
                column_name = "Z" + column_name
                columnNumber -= 26
                division = columnNumber // 26
            if division == 0:
                break
            columnNumber = division
        return column_name
