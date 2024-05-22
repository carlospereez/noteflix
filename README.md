# noteflix

Noteflix es una aplicación de simulación 
de visualización de contenido multimedia. 
Permite a los usuarios visualizar 
películas y series, 
obtener recomendaciones y ver estadísticas 
de visualización.

## Características

- Creación y gestión de usuarios.
- Visualización de películas y series.
- Obtención de recomendaciones basadas en las visualizaciones del usuario.
- Visualización de estadísticas de visualización del usuario.

## Arquitectura del Proyecto

Noteflix sigue una arquitectura de diseño
modular, lo que significa que el código 
está organizado en módulos o componentes 
independientes que realizan tareas 
específicas. Esta arquitectura tiene varias ventajas:

- **Separación de responsabilidades**: Cada módulo se encarga de una parte específica de la funcionalidad de la aplicación, lo que facilita la comprensión y el mantenimiento del código.

- **Reutilización de código**: Los módulos pueden ser reutilizados en diferentes partes de la aplicación, lo que reduce la duplicación de código.

- **Facilita las pruebas**: Los módulos pueden ser probados de manera independiente, lo que facilita la detección y corrección de errores.

- **Flexibilidad**: Los módulos pueden ser modificados, añadidos o eliminados sin afectar al resto de la aplicación, lo que facilita la evolución y adaptación de la aplicación a nuevas necesidades.

La aplicación se divide en varios módulos principales:

- **Modelo**: Contiene las clases que representan las entidades del dominio de la aplicación, como Usuario, Película, Serie, etc.

- **Servicio**: Contiene las clases que implementan la lógica de negocio de la aplicación, como la gestión de usuarios, la visualización de películas y series, la generación de recomendaciones, etc.

- **Vista**: Contiene las clases que se encargan de la interacción con el usuario, como la muestra de menús y la recogida de datos del usuario.

- **Repositorio**: Contiene las clases que se encargan de la persistencia de los datos de la aplicación.


Cada uno de estos módulos se implementa en su propio paquete de Python, lo que facilita la organización y localización del código.