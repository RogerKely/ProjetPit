-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost
-- Généré le : mar. 14 mai 2024 à 14:39
-- Version du serveur : 10.4.28-MariaDB
-- Version de PHP : 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `examen_python_election`
--

-- --------------------------------------------------------

--
-- Structure de la table `candidat`
--

CREATE TABLE `candidat` (
  `id_candidat` int(11) NOT NULL,
  `nom_candidat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `candidat`
--

INSERT INTO `candidat` (`id_candidat`, `nom_candidat`) VALUES
(1, 'Andry RATSIVAHINY'),
(2, 'GASCAR Fenosoa'),
(3, 'RAFARALAHY Doara');

-- --------------------------------------------------------

--
-- Structure de la table `listeVote`
--

CREATE TABLE `listeVote` (
  `id_liste` int(11) NOT NULL,
  `id_candidat` int(11) NOT NULL,
  `nom_candidat` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `listeVote`
--

INSERT INTO `listeVote` (`id_liste`, `id_candidat`, `nom_candidat`) VALUES
(1, 1, 'Andry RATSIVAHINY'),
(2, 1, 'Andry RATSIVAHINY'),
(3, 2, 'GASCAR Fenosoa'),
(4, 1, 'Andry RATSIVAHINY'),
(5, 3, 'RAFARALAHY Doara'),
(6, 2, 'GASCAR Fenosoa'),
(7, 2, 'GASCAR Fenosoa'),
(8, 2, 'GASCAR Fenosoa'),
(9, 2, 'GASCAR Fenosoa');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `candidat`
--
ALTER TABLE `candidat`
  ADD PRIMARY KEY (`id_candidat`);

--
-- Index pour la table `listeVote`
--
ALTER TABLE `listeVote`
  ADD PRIMARY KEY (`id_liste`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `candidat`
--
ALTER TABLE `candidat`
  MODIFY `id_candidat` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT pour la table `listeVote`
--
ALTER TABLE `listeVote`
  MODIFY `id_liste` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
