# Exercice 1 : Favorite Numbers (sets)
# 1. Crée un set "my_fav_numbers" avec tes nombres favoris
# 2. Ajoute deux nouveaux nombres au set
# 3. Retire le dernier nombre que tu viens d'ajouter
# 4. Crée un autre set "friend_fav_numbers" avec les favoris de ton ami
# 5. Fusionne les deux dans un nouveau set "our_fav_numbers"



favorite_set= {6,13,666}
friend_fav_numbers = {2,1000,379}
favorite_set.add(999)
favorite_set.add(333)
favorite_set.remove(333)
our_fav_numbers = favorite_set|friend_fav_numbers
print(our_fav_numbers)
