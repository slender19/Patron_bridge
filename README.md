#  Patrón Bridge — Sistema de Notificaciones Corporativas (NotiCorp)

## Contexto

Una empresa grande (por ejemplo, una plataforma de educación en línea) necesita un **sistema de notificaciones** para comunicarse con usuarios: avisos críticos, recordatorios de cursos, promociones y resúmenes.  

Las notificaciones se crean a partir de distintos **tipos** (Alertas, Recordatorios, Boletines) y deben ser enviadas por distintos **canales** (Email, SMS, Push, WhatsApp, Webhook).  

La empresa quiere poder añadir **nuevos tipos de notificaciones** y **nuevos canales de entrega** de forma independiente, sin modificar mucho código existente.

---

## Problema

Si se implementan combinaciones concretas (por ejemplo `EmailAlert`, `SMSReminder`, `PushNewsletter`), el número de clases crece **combinatoriamente** cuando se añaden tipos o canales.  

Además:

- Los requisitos de formato del mensaje (plantilla, prioridad, enriquecimiento de contenido) los define **el tipo de notificación**.  
- El envío concreto (autenticación, reintentos, logs, métricas) lo gestiona **el canal**.  
- En tiempo de ejecución puede ser necesario **cambiar el canal por defecto** para una notificación (ej. si falla el SMS, usar Email).  
- Se requiere soporte para permitir que **clientes o módulos externos seleccionen dinámicamente** el canal y tipo.

---

## Requisitos funcionales

1. Crear notificaciones de tipos: **Alerta**, **Recordatorio**, **Boletín** (pueden añadirse más).  
2. Enviar notificaciones por canales: **Email**, **SMS**, **Push**, **WhatsApp**, **Webhook** (pueden añadirse más).  
3. Permitir que cada notificación use **cualquier canal** (combinaciones libres).  
4. Permitir **cambiar o añadir canales sin modificar las clases de tipos**.  
5. Soportar **políticas de reintento y logging por canal**.  
6. Permitir que en caso de fallo de envío se intente **un canal alternativo configurado**.

---

## Requisitos no funcionales

- **Fácil extensión:** añadir nuevos tipos o canales sin afectar al código existente.  
- **Bajo acoplamiento:** entre “qué” se envía (tipo) y “cómo” se envía (canal).  
- **Buena mantenibilidad y testabilidad.**  
- **Rendimiento suficiente:** posibilidad de integrar envíos asíncronos (colas de mensajes).

---

## Diseño UML

![UML Bridge Pattern](https://github.com/user-attachments/assets/5f051654-0b80-479a-9b6f-bad7d2ca3263)

---

## Patrón aplicado: Bridge

El patrón **Bridge** desacopla una abstracción (tipos de notificación) de su implementación (canales de envío), permitiendo que ambos evolucionen **independientemente**.  

Esto facilita mantener el sistema modular, extensible y flexible ante nuevas integraciones o tecnologías de comunicación.

---

✍️ **Autor:** *Walfran Martinez y Alexander Amaya*  
📅 **Proyecto:** Implementación del Patrón Bridge — NotiCorp
