def search_substring(haystack, needle):
    if not haystack or not needle:
        return []

    def build_transition_table(needle):
        m = len(needle)
        alphabet = set(needle)
        transition_table = {}

        for state in range(m + 1):
            for char in alphabet:
                prefix = min(m, state + 1)
                while prefix > 0 and needle[:prefix] != needle[state - prefix + 1:state] + char:
                    prefix -= 1
                transition_table[state, char] = prefix

        return transition_table

    def search_using_fsm(haystack, needle, transition_table):
        n, m = len(haystack), len(needle)
        indices = []
        state = 0

        for i in range(n):
            state = transition_table.get((state, haystack[i]), 0)

            if state == m:
                indices.append(i - m + 1)

        return indices

    transition_table = build_transition_table(needle)
    result = search_using_fsm(haystack, needle, transition_table)
    return result
