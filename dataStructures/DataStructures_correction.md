## Exercise 1 - Class methods & Namedtuple

### Question 1

```
Card = collections.namedtuple("Card", ['rank', 'suit'])

suits = "spades diamonds hearts clubs".split(" ")
ranks = [str(n) for n in range(2, 11)] + list('JQKA')

cards = [Card(rank, suit) for suit in self.suits
                          for rank in self.ranks]

```

### Question 2 & 3

```
class Deck:
    def __init__(self):
        self._cards = cards
        self.sorting = dict(spades=3, diamonds=2, hearts=1, clubs=0)

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]
        
    def card_value(self, card):
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.sorting) + self.sorting[card.suit]
```

### Question 4

```
def sort_cards_by_value(deck):
    return sorted(deck, key=deck.card_value)
```

## Exercise 2 - Sets

### Question 1

```
candidates = {
    "Bob": {"Python", "C++", "SQL", "Flask"},
    "Peter": {"Python", "C#", "Javascript"},
    "Alice": {"C++", "React", "SQL"},
    "Lily": {"SQL", "Python", "Flask", "Lua"}
}

class ManageCandidates:
    def __init__(self, candidates):
        self.candidates = candidates
    
    def add_candidate(self, name, skills):
        self.candidates[name] = skills
    
    def remove_candidate(self, name):
        del self.candidates[name]
    
    def add_skill(self, name, skill):
        self.candidates[name].add(skill)
    
    def remove_skill(self, name, skill):
        self.candidates[name].remove(skill)
    
    def get_all_skills(self):
        all_skills = set()
        for skills in self.candidates.values():
            all_skills.update(skills)
        return all_skills
    
    def common_skills(self, *names):
        common = self.candidates[names[0]]
        for name in names[1:]:
            common.intersection_update(self.candidates[name])
        return common
    
    def lacking_skills(self, name):
        return self.get_all_skills().difference(self.candidates[name])
    
    def get_experts(self, skill):
        experts = []
        for name, skills in candidates.items():
            if skill in skills:
                experts.append(name)
        return experts
    
    def reverse_candidates(self):
        reverse_candidates = {}
        for name, skills in candidates.items():
            for skill in skills:
                reverse_candidates.setdefault(skill, set()).add(name)
        return reverse_candidates
```

### Question 2

```
mc = ManageCandidates(candidates)

experts = mc.get_experts("Python")
print("Python experts:", experts)

print("Common skills:", mc.common_skills(*experts))
if experts:
    lacking = mc.lacking_skills(experts[0])
    for expert in experts[1:]:
        lacking.intersection_update(mc.lacking_skills(expert)) 
    print("Lacking skills:", lacking)
```
