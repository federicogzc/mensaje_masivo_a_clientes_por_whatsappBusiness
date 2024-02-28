<h2>🚀 Guía de inicio rápido</h2>
<p>Esta guía te ayudará a configurar y ejecutar un programa en Python para enviar mensajes a través de WhatsApp utilizando una API. Ideal para notificaciones automáticas, marketing, o cualquier otro caso de uso que requiera comunicación directa.</p>
<p> Debes tener en cuenta que lo primero que tienes que hacer es configurar tu cuenta y permisos de  facebook.business  https://business.facebook.com</p>

<h3>🔧 Pre-requisitos</h3>
<ul>
  <li>Python 3.6 o superior.</li>
  <li>Pandas: Una biblioteca de Python para manipulación de datos.</li>
  <li>Requests: Una biblioteca de Python para realizar solicitudes HTTP.</li>
</ul>

<h3>📦 Instalación de Dependencias</h3>
<p>Antes de ejecutar el programa, necesitas instalar las dependencias requeridas. Abre tu terminal y ejecuta el siguiente comando:</p>

<pre><code>pip install pandas requests</code></pre>

<h3>🔑 Configuración de la API</h3>
<p>Para utilizar la API de WhatsApp, necesitas configurar tus credenciales. Sigue estos pasos:</p>
<ol>
  <li>Obtén tu <strong>TOKEN</strong> y <strong>URL</strong> de la API de WhatsApp al registrarte en el servicio de WhatsApp Business API.</li>
  <li>Reemplaza <code>"https://graph.facebook.com/v12.0/201848473684/messages"</code> en la variable <code>WHATSAPP_API_URL</code> con tu URL proporcionada.</li>
  <li>Reemplaza <code>"here you put the key"</code> en la variable <code>TOKEN</code> con tu token de acceso.</li>
</ol>

<h3>📝 Uso del Programa</h3>
<p>El programa consta de dos partes principales:</p>
<ul>
  <li><strong>Envío de mensajes:</strong> Define la función <code>enviar_mensaje_plantilla_whatsapp</code> para enviar mensajes a través de WhatsApp utilizando plantillas predefinidas.</li>
  <li><strong>Lectura y envío automático:</strong> La función <code>leer_numeros_celular_y_enviar_mensaje</code> lee números de teléfono de un archivo CSV y envía un mensaje a cada número utilizando una plantilla predefinida.</li>
</ul>

<h4>Cómo ejecutar:</h4>
<ol>
  <li>Coloca tu archivo CSV con números de teléfono en el directorio <code>/app/data/</code>. Asegúrate de que el archivo use <code>;</code> como separador.</li>
  <li>Abre tu terminal, navega al directorio donde se encuentra el script y ejecútalo con Python:</li>
</ol>

<pre><code>python tu_script.py</code></pre>

<h3>🔄 Personalización</h3>
<p>Puedes personalizar el mensaje editando la plantilla en la función <code>enviar_mensaje_plantilla_whatsapp</code>. Asegúrate de cambiar <code>"tu_namespace_aquí"</code> por tu namespace de plantilla y <code>"inspeccion_notificacion"</code> por el nombre de tu plantilla real.</p>

<h3>🛠️ Soporte</h3>
<p>Si tienes preguntas o necesitas ayuda con la configuración, no dudes en consultar la documentación oficial de la API de WhatsApp o contactar a su soporte técnico.</p>

<h3>💡 Consejos</h3>
<ul>
  <li>Asegúrate de seguir las políticas de uso de la API de WhatsApp para evitar el bloqueo o la suspensión de tu cuenta.</li>
  <li>Realiza pruebas con números de teléfono de prueba antes de lanzar una campaña masiva.</li>
</ul>

<h3>👍 ¡Listo!</h3>
<p>Ahora estás listo para utilizar este programa para mejorar la comunicación con tus clientes o usuarios a través de WhatsApp. ¡Explora las posibilidades!</p>
