class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # verify we can make the groups
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        # sort the list
        hand.sort()

        # greedily make groups
        for num in hand:
            if count[num]:
                # these need to be the rest of the numbers so check if in hand
                for i in range(num, num + groupSize):
                    if count[i]:
                        count[i] -= 1
                    else:
                        return False

        return True


        
            