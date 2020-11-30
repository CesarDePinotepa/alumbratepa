-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 30, 2020 at 09:07 PM
-- Server version: 5.7.31
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `alumbradopino`
--

-- --------------------------------------------------------

--
-- Table structure for table `reporte`
--

DROP TABLE IF EXISTS `reporte`;
CREATE TABLE IF NOT EXISTS `reporte` (
  `id_reporte` int(11) NOT NULL AUTO_INCREMENT,
  `numero_reporte` varchar(20) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `status` varchar(45) NOT NULL,
  `fecha` date NOT NULL,
  `poste` varchar(20) NOT NULL,
  `funcionamiento` varchar(45) NOT NULL,
  `comentario` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id_reporte`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `reporte`
--

INSERT INTO `reporte` (`id_reporte`, `numero_reporte`, `direccion`, `status`, `fecha`, `poste`, `funcionamiento`, `comentario`, `user_id`) VALUES
(1, '1', 'Calle 7, Colonia Siete, Pinotepa Nal ', 'Atendido', '2020-11-01', 'PO-1896', 'Apagado', 'Lleva tres dias sin prender', 5),
(3, 'AP-2020-11-2013', 'Calle 13 , Col. Centro, Pinotepa Nacional', 'Activo', '2020-11-20', '16516', 'Poste Caido', 'El poste lo tiro un carro', 5);

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `tipo` char(1) NOT NULL,
  `password` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `email`, `tipo`, `password`) VALUES
(5, 'Nacho', 'Vargas', 'nacho@email.com', '0', 'df60b4335cfeb79760369df76b7c374d'),
(6, 'Hugo', 'Sanchez', 'hugo@email.com', '0', '29b3e3880a787d0f95d4ee0b6931813d'),
(7, 'Ismael', 'de la Fuente', 'isma@email.com', '0', 'b51a3f14bdf29a854a17bd9a1431c7e9'),
(8, 'Vanesa', 'Zamora', 'vane@email.com', '0', '47fb60b814b8a64efcf9023cdee246bf'),
(9, 'Erick', 'Aleman', 'aleman@mail.com', '0', '7d4b7aea7ba8a761ea8063236c734f54'),
(10, 'Paola', 'Espinoza', 'pao@gmail.com', '0', 'af4832e0dc4887857225b3ed0e4cc5aa'),
(11, 'Eli ', 'Cielo Nublado', 'eli@mail.com', '1', '95b32488ded4e6d0df683abff6c5f4e7'),
(12, 'Admin', 'Administrador', 'admin@mail.com', '1', '4441e5d70b3657900fa57e66db407e0b');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
