-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : jeu. 25 juin 2026 à 10:13
-- Version du serveur : 8.0.31
-- Version de PHP : 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `tomodachimac`
--

-- --------------------------------------------------------

--
-- Structure de la table `compte`
--

DROP TABLE IF EXISTS `compte`;
CREATE TABLE IF NOT EXISTS `compte` (
  `id_compte` int NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(99) NOT NULL,
  `mdp` varchar(99) NOT NULL,
  PRIMARY KEY (`id_compte`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `compte`
--

INSERT INTO `compte` (`id_compte`, `pseudo`, `mdp`) VALUES
(4, 'lebron', '119c9ae6f9ca741bd0a76f87fba0b22cab5413187afb2906aa2875c38e213603'),
(3, 'cerise', '4ec7c53222c8a758c722e2111541035ce700d5ae7bd0898c5f1b1a743e6450fd');

-- --------------------------------------------------------

--
-- Structure de la table `famille`
--

DROP TABLE IF EXISTS `famille`;
CREATE TABLE IF NOT EXISTS `famille` (
  `id_famille` int NOT NULL AUTO_INCREMENT,
  `nom_famille` text NOT NULL,
  PRIMARY KEY (`id_famille`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `ile`
--

DROP TABLE IF EXISTS `ile`;
CREATE TABLE IF NOT EXISTS `ile` (
  `id_ile` int NOT NULL AUTO_INCREMENT,
  `nom_ile` varchar(99) NOT NULL,
  `id_compte` int NOT NULL COMMENT 'cle etrangere',
  `note` int NOT NULL COMMENT 'cle etrangere',
  PRIMARY KEY (`id_ile`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `ile`
--

INSERT INTO `ile` (`id_ile`, `nom_ile`, `id_compte`, `note`) VALUES
(5, 'LEBRON ILAND YEAHHH', 4, 0),
(4, 'IMAC 1', 3, 0);

-- --------------------------------------------------------

--
-- Structure de la table `mii`
--

DROP TABLE IF EXISTS `mii`;
CREATE TABLE IF NOT EXISTS `mii` (
  `id_mii` int NOT NULL AUTO_INCREMENT,
  `nom_mii` varchar(99) NOT NULL,
  `age` int NOT NULL,
  `image` text,
  `id_ile` int NOT NULL COMMENT 'cle etrangere',
  `sexe` text NOT NULL,
  `personnalite` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `id_famille` int DEFAULT NULL COMMENT '#',
  `id_pere` int DEFAULT NULL COMMENT '#',
  `id_mere` int DEFAULT NULL COMMENT '#',
  `id_partenaire` int DEFAULT NULL COMMENT '#',
  `id_crush` int DEFAULT NULL COMMENT '#',
  PRIMARY KEY (`id_mii`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `mii`
--

INSERT INTO `mii` (`id_mii`, `nom_mii`, `age`, `image`, `id_ile`, `sexe`, `personnalite`, `id_famille`, `id_pere`, `id_mere`, `id_partenaire`, `id_crush`) VALUES
(3, 'Marine', 67, '673cb99d3ee95b481da0c6142d652645.jpg', 4, 'woman', 'reserved', NULL, NULL, NULL, NULL, NULL),
(4, 'lou', 77, 'images.jpg', 4, 'man', 'outgoing', NULL, NULL, NULL, NULL, NULL),
(5, 'basketball', 21, '17500.jpg', 5, 'man', 'considerate', NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Structure de la table `note`
--

DROP TABLE IF EXISTS `note`;
CREATE TABLE IF NOT EXISTS `note` (
  `id_note` int NOT NULL AUTO_INCREMENT,
  `note` int NOT NULL,
  `id_ile` int NOT NULL COMMENT 'cle etrangere',
  PRIMARY KEY (`id_note`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `note`
--

INSERT INTO `note` (`id_note`, `note`, `id_ile`) VALUES
(7, 3, 5),
(6, 2, 5),
(5, 5, 4);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
