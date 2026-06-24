-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le : mer. 24 juin 2026 à 08:34
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
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `compte`
--

INSERT INTO `compte` (`id_compte`, `pseudo`, `mdp`) VALUES
(1, 'lebron', '119c9ae6f9ca741bd0a76f87fba0b22cab5413187afb2906aa2875c38e213603'),
(2, 'big yahu', 'b5f044fbe895c22a619df2f398add6cd3e7252a517dac22ecdb27c54089ff7fa');

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
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `mii`
--

DROP TABLE IF EXISTS `mii`;
CREATE TABLE IF NOT EXISTS `mii` (
  `id_mii` int NOT NULL AUTO_INCREMENT,
  `nom_mii` varchar(99) NOT NULL,
  `sexe` enum('M','F') NOT NULL,
  `age` int NOT NULL,
  `image` int DEFAULT NULL,
  `id_ile` int NOT NULL COMMENT 'cle etrangere',
  PRIMARY KEY (`id_mii`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
