# DROP TABLE IF EXISTS `Item`;
# DROP TABLE IF EXISTS `Type`;
# DROP TABLE IF EXISTS `Emprunt`;
# DROP TABLE IF EXISTS `Genre`;
# DROP TABLE IF EXISTS `Auteur`;
# DROP TABLE IF EXISTS `Utilisateur`;

CREATE TABLE `Item` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(50),
  `type_id` integer,
  `auteur_id` integer,
  `genre_id` integer,
  `emprunt_id` integer,
  `created_at` timestamp
);

CREATE TABLE `Type` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `number` integer
);

CREATE TABLE `Emprunt` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `emprunt` bool,
  `date_debut` date,
  `date_fin` date,
  `user_id` integer
);

CREATE TABLE `Genre` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nom` varchar(50),
  `prenom` varchar(50)
);

CREATE TABLE `Auteur` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nom` varchar(50),
  `prenom` varchar(50)
);

CREATE TABLE `Utilisateur` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nom` varchar(50),
  `prenom` varchar(50),
  `created_at` timestamp
);

ALTER TABLE `Item` ADD FOREIGN KEY (`type_id`) REFERENCES `Type` (`id`);
ALTER TABLE `Item` ADD FOREIGN KEY (`auteur_id`) REFERENCES `Auteur` (`id`);
ALTER TABLE `Item` ADD FOREIGN KEY (`genre_id`) REFERENCES `Genre` (`id`);
ALTER TABLE `Item` ADD FOREIGN KEY (`emprunt_id`) REFERENCES `Emprunt` (`id`);
ALTER TABLE `Emprunt` ADD FOREIGN KEY (`user_id`) REFERENCES `Utilisateur` (`id`);
