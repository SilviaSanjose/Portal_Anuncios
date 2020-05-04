-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 04-05-2020 a las 18:43:31
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_anuncios_manualidades`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_admin`
--

CREATE TABLE `tabla_admin` (
  `ID` int(11) NOT NULL,
  `USER` varchar(30) NOT NULL,
  `PASSWD` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_admin`
--

INSERT INTO `tabla_admin` (`ID`, `USER`, `PASSWD`) VALUES
(2, 'mabel', '1615'),
(4, 'ares', 'ares');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_anuncios`
--

CREATE TABLE `tabla_anuncios` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(100) NOT NULL,
  `CATEGORIA` int(11) NOT NULL,
  `PRECIO` decimal(6,2) NOT NULL,
  `DESCRIPCION` varchar(300) NOT NULL,
  `ENVIO` varchar(2) NOT NULL,
  `CONTACTO` varchar(255) NOT NULL,
  `EMAIL-VALIDADO` varchar(2) NOT NULL DEFAULT 'No',
  `CODIGO` varchar(255) NOT NULL DEFAULT 'No'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_anuncios`
--

INSERT INTO `tabla_anuncios` (`ID`, `NOMBRE`, `CATEGORIA`, `PRECIO`, `DESCRIPCION`, `ENVIO`, `CONTACTO`, `EMAIL-VALIDADO`, `CODIGO`) VALUES
(1, 'Camiseta Spiderman', 1, '12.00', 'Camiseta de niñ@ manga corta', 'Si', 'mabel@gmail.com', '0', 'No'),
(2, 'Centro Mesa', 3, '20.00', 'Centro de mesa de navidad, hecho a mano. Posibilidad de personalizar', 'Si', 'mabel@gmail.com', '0', 'No'),
(4, 'Bolso de mano', 2, '15.20', 'Bolso de mano morado, con adornos', 'No', 'mabel@gmail.com', '0', 'No'),
(10, 'Pendientes Gato', 2, '13.20', 'Pendientes de gato, con el cuerpo colgando por detrás.', 'No', 'mabel@gmail.com', '0', 'No'),
(17, 'Collar madera', 2, '12.00', 'collar de madera artesalanl', 'No', 'pideseloasilvi@gmail.com', 'NO', 'u2q7wM1Gk4Pyam1UkrfedECMKy2SBLRu8Eg4jAyEcZKMQSPKUNPHEoQWxKOKpnnx2fhwGHjtBl6176RR3InLDYNGgo72aneV5aZcfnnTUVuMBl0o1JyBH7RwcP3DolXQjPqP8H4hJyxqyM9PiBfcZkvWuYi7RU6R1RmgiYI7vRYXGnjhMLziFYlBhSuiMUnCmtGSyAXn'),
(21, 'Camiseta de Sonic', 1, '18.50', 'Camiseta de manga corta, de Sonic, bordada a mano', 'Si', 'pideseloasilvi@gmail.com', 'Si', '2r2U9hOOP1Q6rUORKvU3CycwEIfKIrOr4awSAIK1iRKrMfkSQe0WUdAEdLdqFI9yZEH5hrhNdK3U0d9KD0VZGg3GeZxvaXqVw6Rostyqj6yncbN1I5c7K2VTxlwRFgJqFE1ZIhUjXPewDZCTqZOxD1Uy0YHqe4qUbACyldRHBXJiCk9kTJaUrrBwR61bygk9bX1mxZeQ'),
(23, 'Manta', 2, '15.90', 'dfdfdfgd', 'Si', 'pideseloasilvi@gmail.com', 'Si', 'M6zqcqWrn8DxIWHdMvE7t3oQ63wFGdKygSYepTw4q2t68Caq7kVXNdo3DnY9L87aO1RIWsmTUOM39ctDv7h9QOSUpYaAaRIQ6YQERSJn0kqJ16zKXibfvU2YfexNfQsDXJ12b3G8CmekWuwHhu4CpBUstISq0Gqaa9UzP0DISQaPUA28JfrFq0F8yQ8VbDhPsuM3OGxD'),
(24, 'Collar de Macarrones', 2, '9.00', 'Te lo pones o te lo comes!', 'Si', 'pideseloasilvi@gmail.com', 'Si', 'L40L9RODFzX60OFtsBIuacJB0jtplvmNoh635lM86U1TN4Thl7zKBxzK3incE1MHiestq5s2H2eTxFHFMMaKCf4zDD7dOI2o7AIRpaGIxDlHxG8XrtcsLErzJ6wIKMEQ90zE5RfEW5V6q4Riip6u7aOmVIJ5SstQZLoMlAqESI8K81AZAHVuqzuk2vwqIJMlzNsIwenm'),
(26, 'Bolso morado', 1, '15.00', 'Bolso de mano, morado, con bordado de flores. Tiene una cinta para poder sujetar.', 'Si', 'pideseloasilvi@gmail.com', 'Si', 'DwzKCMvebTIfAHwmt3N1PCDuhdR5sWwn3JST7uZtBjZRVG6hv5q5F8vNFKArMKozPPXFfDSQqyxTbqcxAXuMY9OXW65iWFcWhUD9oQG2AJXOt63jTqPqTu2IkK8om6KNaOmZTSa3J3Iz3sT8kaAXeYYEO2ZZFcIYFQKlgdrhNR3rqd6lsIBIWPzE3rQXY0nqKPzR5NQg'),
(27, 'Máscara chica', 3, '16.30', 'Máscara hecha con tela, color bronce. ', 'Si', 'pideseloasilvi@gmail.com', 'Si', 'UlWbENSReOzseoQwtOa9LHAtDLUBz8W3dVzgskF5JUcJ49Eb40N0gyn95WyDC3cDJJcm2mbb0JqaprpgFC9WtjTJDv11sSjEmciJ3yIvgdWiWXs4RAYJRHQKZdcVmyS5zS8CjEbVQieOrqXkFABdWAVhdZySJs4kOgLRsWxwleA9FptVN4tHjV5dmcszgmXcCW6zvN9A'),
(28, 'Máscara Plata', 3, '16.00', 'mascara de tela', 'Si', 'pideseloasilvi@gmail.com', 'Si', '2OEpqzZHj5XcgQ3FesYVv8ynnvVBb2FVzkQUA14lm8B4ryzKtVSOWJecYbjTHj5bAlCUpKApxkTbk99TOBovvtKwiUVvBzJNEPGcGsjYo7OSHy9k3fCIBY4ZVyYT9UQVxhi2JAu8qlL5FujEuJKh3cpXnvQZj7Ry7DWt2kJ325h1Q6zSE1pby3kdF4Y1jPA4sRJGjYYN');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_categorias`
--

CREATE TABLE `tabla_categorias` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_categorias`
--

INSERT INTO `tabla_categorias` (`ID`, `NOMBRE`) VALUES
(1, 'Ropa'),
(2, 'Complementos'),
(3, 'Decoración');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_chat`
--

CREATE TABLE `tabla_chat` (
  `ID` int(11) NOT NULL,
  `NOMBRE` varchar(50) NOT NULL,
  `MENSAJE` varchar(2000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_chat`
--

INSERT INTO `tabla_chat` (`ID`, `NOMBRE`, `MENSAJE`) VALUES
(1, 'Silvi', 'Buenos días'),
(2, 'Ampo', 'Hola'),
(3, 'Silvi', 'hace sol!!'),
(4, 'Ampo', 'Siii'),
(5, 'Silvia', 'Ya lo tengo!!!'),
(6, 'Juli', 'Hola'),
(7, 'Juana', 'Buenos días!'),
(8, 'pepe', 'que tal'),
(9, 'Juana', 'holaaaaaaa\n'),
(10, 'Silvita', 'Hola'),
(11, 'Silvi', 'Hola'),
(12, 'Pepe', 'Aquí estamos'),
(13, 'Laura', 'Hola a todos'),
(14, 'Ampo', 'Que tal?'),
(15, 'Maribel', 'Buenasss');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_admin`
--
ALTER TABLE `tabla_admin`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `tabla_anuncios`
--
ALTER TABLE `tabla_anuncios`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `CATEGORIA` (`CATEGORIA`);

--
-- Indices de la tabla `tabla_categorias`
--
ALTER TABLE `tabla_categorias`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `tabla_chat`
--
ALTER TABLE `tabla_chat`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_admin`
--
ALTER TABLE `tabla_admin`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `tabla_anuncios`
--
ALTER TABLE `tabla_anuncios`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `tabla_categorias`
--
ALTER TABLE `tabla_categorias`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `tabla_chat`
--
ALTER TABLE `tabla_chat`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `tabla_anuncios`
--
ALTER TABLE `tabla_anuncios`
  ADD CONSTRAINT `tabla_anuncios_ibfk_1` FOREIGN KEY (`CATEGORIA`) REFERENCES `tabla_categorias` (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
