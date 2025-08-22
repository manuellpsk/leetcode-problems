class Solution:
    def generateTag(self, caption: str) -> str:
        caps = caption.split()
        if not caps:
            return "#"
        output = "#" + caps[0].lower()
        for cap in caps[1:]:
            output += cap.title()
        if len(output) > 100:
            return output[:100]
        return output
