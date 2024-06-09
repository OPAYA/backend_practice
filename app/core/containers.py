from dependency_injector import providers, containers

from app.core.config import BaseAppSettings

import app.services as services
import app.db.repositories as repositories


class Container(containers.DeclarativeContainer):
    config: BaseAppSettings = providers.Configuration()

    wiring_config = containers.WiringConfiguration(
        packages=[
            "app.api",
            "app.api.v1",
            "app.core",
            "app.services",
        ]
    )
    
    item_repository = providers.Factory(repositories.ItemRepository)
    
    item_service = providers.Factory(
        services.ItemService,
        item_repository=item_repository
    )