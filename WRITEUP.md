# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.
*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

## Comparison: VM vs App Service

| Feature            | Virtual Machine (VM)                                  | App Service                                           |
|--------------------|--------------------------------------------------------|--------------------------------------------------------|
| **Cost**           | Higher operational cost due to continuous uptime billing and manual scaling. | Lower cost with consumption-based pricing and built-in scaling. |
| **Scalability**    | Manual configuration required. | Automatic scaling based on demand, with minimal configuration. |
| **Availability**   | Requires setup of availability zones and redundancy. | High availability is built-in with Azure infrastructure. |
| **Security**       | Full control over OS-level security, but requires manual patching and updates. | Managed platform with automatic updates and integrated security features. |
| **Deployment**     | Manual deployment via SSH or custom scripts.           | Seamless CI/CD integration with GitHub. |
| **Maintenance**    | Requires ongoing OS and software maintenance.          | Fully managed environment with minimal maintenance overhead. |
| **Use Case Fit**   | Suitable for complex, custom environments or legacy apps. | Ideal for modern web apps and APIs with standard frameworks. |

## Decision and Justification

For this project, I chose **Azure App Service** to deploy the FlaskWebProject. The main reasons are:

- **Ease of Deployment**: App Service integrates directly with GitHub, allowing for automated deployments and version control.
- **Managed Infrastructure**: It abstracts away the need to manage VMs, OS updates, and scaling configurations.
- **Cost Efficiency**: App Service offers a more economical model for lightweight web applications, especially during development and testing.
- **Built-in Features**: Features like custom domains, SSL, authentication, and monitoring are readily available and easy to configure.

Given the simplicity and requirements of the Flask CMS application, App Service provides a faster, more scalable, and cost-effective solution compared to a VM.

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

Although Azure App Service works great for lightweight web apps like the one in this project, there are scenarios where switching to a VM might make more sense. For example, if the app needed a custom OS or runtime, handled high-performance workloads, had complex networking needs, required persistent local storage, integrated with legacy software, or had strict security and compliance requirements—then a VM would be a better fit.
If the application evolves to require more control over the environment, specialized hardware, or complex configurations, switching to a VM would be justified.