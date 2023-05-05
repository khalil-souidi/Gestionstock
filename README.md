Application de gestion de stock développée en Python avec la bibliothèque de GUI Tkinter pour créer les interfaces utilisateur, et une base de données relationnelle MySQL avec PHPMyAdmin pour stocker les informations sur les produits et les utilisateurs.

L'application permet aux utilisateurs de créer un compte avec un nom d'utilisateur et un mot de passe en utilisant le bouton "signup".
Elle permet également aux utilisateurs de se connecter avec leur nom d'utilisateur et leur mot de passe en utilisant le bouton "signin".
Elle affiche la liste des produits avec les attributs suivants : (ID, Nom, Description, Prix, Quantité, Date de dernière entrée en stock).
Les utilisateurs peuvent ajouter des produits en utilisant le bouton "ADD", modifier des produits en utilisant leur ID en utilisant le bouton "update", et supprimer des produits en utilisant leur nom en utilisant le bouton "delete". 
Les utilisateurs peuvent également rechercher des produits par nom, prix, quantité et date de dernière entrée en stock en utilisant le bouton "search" et la liste déroulante. Les informations des utilisateurs et des produits sont stockées dans une table de la base de données. 
Les utilisateurs peuvent se déconnecter ou quitter le programme en utilisant la barre de navigation.

Lors du login Si le nom d'utilisateur ou le mot de passe n'existe pas, un message d'erreur s'affiche. Sinon, l'accès est autorisé.

Lors de la création d'un nouveau compte, si le nom d'utilisateur existe déjà dans la base de données, un message d'erreur s'affiche.Si les deux mots de passe ne sont pas identiques, un message d'erreur s'affiche également. Dans le cas contraire, l'accès est autorisé.

Lors de l'ajout d'un produit, si l'ID existe déjà dans la base de données, un message d'erreur s'affiche. Si la quantité est inférieure ou égale à 5, un message d'alerte s'affiche, mais le produit est ajouté à la base de données quand même.
