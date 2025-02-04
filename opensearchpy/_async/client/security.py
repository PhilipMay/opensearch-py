# SPDX-License-Identifier: Apache-2.0
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
#
# Modifications Copyright OpenSearch Contributors. See
# GitHub history for details.

# ------------------------------------------------------------------------------------------
# THIS CODE IS AUTOMATICALLY GENERATED AND MANUAL EDITS WILL BE LOST
#
# To contribute, kindly make modifications in the opensearch-py client generator
# or in the OpenSearch API specification, and run `nox -rs generate`. See DEVELOPER_GUIDE.md
# and https://github.com/opensearch-project/opensearch-api-specification for details.
# -----------------------------------------------------------------------------------------+


from typing import Any

from .utils import SKIP_IN_PATH, NamespacedClient, _make_path, query_params


class SecurityClient(NamespacedClient):
    from ._patch import health_check, update_audit_config  # type: ignore

    @query_params()
    async def get_account_details(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns account details for the current user.

        """
        return await self.transport.perform_request(
            "GET", "/_plugins/_security/api/account", params=params, headers=headers
        )

    @query_params()
    async def change_password(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Changes the password for the current user.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PUT",
            "/_plugins/_security/api/account",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_action_group(
        self,
        action_group: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves one action group.


        :arg action_group: Action group to retrieve.
        """
        if action_group in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'action_group'."
            )

        return await self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
        )

    @query_params()
    async def get_action_groups(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves all action groups.

        """
        return await self.transport.perform_request(
            "GET",
            "/_plugins/_security/api/actiongroups/",
            params=params,
            headers=headers,
        )

    @query_params()
    async def delete_action_group(
        self,
        action_group: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete a specified action group.


        :arg action_group: Action group to delete.
        """
        if action_group in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'action_group'."
            )

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
        )

    @query_params()
    async def create_action_group(
        self,
        action_group: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or replaces the specified action group.


        :arg action_group: The name of the action group to create or
            replace
        """
        for param in (action_group, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_action_group(
        self,
        action_group: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates individual attributes of an action group.


        """
        for param in (action_group, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "actiongroups", action_group),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_action_groups(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates, updates, or deletes multiple action groups in a single call.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/actiongroups",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_user(
        self,
        username: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieve one internal user.


        """
        if username in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'username'.")

        return await self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
        )

    @query_params()
    async def get_users(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieve all internal users.

        """
        return await self.transport.perform_request(
            "GET",
            "/_plugins/_security/api/internalusers",
            params=params,
            headers=headers,
        )

    @query_params()
    async def delete_user(
        self,
        username: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete the specified user.


        """
        if username in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'username'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
        )

    @query_params()
    async def create_user(
        self,
        username: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or replaces the specified user.


        """
        for param in (username, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_user(
        self,
        username: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates individual attributes of an internal user.


        """
        for param in (username, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "internalusers", username),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_users(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates, updates, or deletes multiple internal users in a single call.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/internalusers",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_role(
        self,
        role: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves one role.


        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return await self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
        )

    @query_params()
    async def get_roles(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves all roles.

        """
        return await self.transport.perform_request(
            "GET", "/_plugins/_security/api/roles/", params=params, headers=headers
        )

    @query_params()
    async def delete_role(
        self,
        role: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete the specified role.


        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
        )

    @query_params()
    async def create_role(
        self,
        role: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or replaces the specified role.


        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_role(
        self,
        role: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates individual attributes of a role.


        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "roles", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_roles(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates, updates, or deletes multiple roles in a single call.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/roles",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_role_mapping(
        self,
        role: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves one role mapping.


        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return await self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
        )

    @query_params()
    async def get_role_mappings(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves all role mappings.

        """
        return await self.transport.perform_request(
            "GET",
            "/_plugins/_security/api/rolesmapping",
            params=params,
            headers=headers,
        )

    @query_params()
    async def delete_role_mapping(
        self,
        role: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes the specified role mapping.


        """
        if role in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'role'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
        )

    @query_params()
    async def create_role_mapping(
        self,
        role: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or replaces the specified role mapping.


        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_role_mapping(
        self,
        role: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates individual attributes of a role mapping.


        """
        for param in (role, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "rolesmapping", role),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_role_mappings(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or updates multiple role mappings in a single call.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/rolesmapping",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_tenant(
        self,
        tenant: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves one tenant.


        """
        if tenant in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'tenant'.")

        return await self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
        )

    @query_params()
    async def get_tenants(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves all tenants.

        """
        return await self.transport.perform_request(
            "GET", "/_plugins/_security/api/tenants/", params=params, headers=headers
        )

    @query_params()
    async def delete_tenant(
        self,
        tenant: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Delete the specified tenant.


        """
        if tenant in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'tenant'.")

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
        )

    @query_params()
    async def create_tenant(
        self,
        tenant: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Creates or replaces the specified tenant.


        """
        for param in (tenant, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_tenant(
        self,
        tenant: Any,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Add, delete, or modify a single tenant.


        """
        for param in (tenant, body):
            if param in SKIP_IN_PATH:
                raise ValueError("Empty value passed for a required argument.")

        return await self.transport.perform_request(
            "PATCH",
            _make_path("_plugins", "_security", "api", "tenants", tenant),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_tenants(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Add, delete, or modify multiple tenants in a single call.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/tenants/",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_configuration(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Returns the current Security plugin configuration in JSON format.

        """
        return await self.transport.perform_request(
            "GET",
            "/_plugins/_security/api/securityconfig",
            params=params,
            headers=headers,
        )

    @query_params()
    async def update_configuration(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Adds or updates the existing configuration using the REST API.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PUT",
            "/_plugins/_security/api/securityconfig/config",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_configuration(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        A PATCH call is used to update the existing configuration using the REST API.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/securityconfig",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def get_distinguished_names(
        self,
        cluster_name: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves all distinguished names in the allow list.


        """
        return await self.transport.perform_request(
            "GET",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
        )

    @query_params()
    async def update_distinguished_names(
        self,
        cluster_name: Any,
        body: Any = None,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Adds or updates the specified distinguished names in the cluster’s or node’s
        allow list.


        """
        if cluster_name in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'cluster_name'."
            )

        return await self.transport.perform_request(
            "PUT",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def delete_distinguished_names(
        self,
        cluster_name: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Deletes all distinguished names in the specified cluster’s or node’s allow
        list.


        """
        if cluster_name in SKIP_IN_PATH:
            raise ValueError(
                "Empty value passed for a required argument 'cluster_name'."
            )

        return await self.transport.perform_request(
            "DELETE",
            _make_path("_plugins", "_security", "api", "nodesdn", cluster_name),
            params=params,
            headers=headers,
        )

    @query_params()
    async def get_certificates(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves the cluster’s security certificates.

        """
        return await self.transport.perform_request(
            "GET", "/_plugins/_security/api/ssl/certs", params=params, headers=headers
        )

    @query_params()
    async def reload_transport_certificates(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Reload transport layer communication certificates.

        """
        return await self.transport.perform_request(
            "PUT",
            "/_plugins/_security/api/ssl/transport/reloadcerts",
            params=params,
            headers=headers,
        )

    @query_params()
    async def reload_http_certificates(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Reload HTTP layer communication certificates.

        """
        return await self.transport.perform_request(
            "PUT",
            "/_plugins/_security/api/ssl/http/reloadcerts",
            params=params,
            headers=headers,
        )

    @query_params()
    async def flush_cache(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Flushes the Security plugin user, authentication, and authorization cache.

        """
        return await self.transport.perform_request(
            "DELETE", "/_plugins/_security/api/cache", params=params, headers=headers
        )

    @query_params()
    async def health(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Checks to see if the Security plugin is up and running.

        """
        return await self.transport.perform_request(
            "GET", "/_plugins/_security/health", params=params, headers=headers
        )

    @query_params()
    async def get_audit_configuration(
        self,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Retrieves the audit configuration.

        """
        return await self.transport.perform_request(
            "GET", "/_plugins/_security/api/audit", params=params, headers=headers
        )

    @query_params()
    async def update_audit_configuration(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Updates the audit configuration.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PUT",
            "/_plugins/_security/api/audit/config",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_audit_configuration(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        A PATCH call is used to update specified fields in the audit configuration.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/audit",
            params=params,
            headers=headers,
            body=body,
        )

    @query_params()
    async def patch_distinguished_names(
        self,
        body: Any,
        params: Any = None,
        headers: Any = None,
    ) -> Any:
        """
        Bulk update of distinguished names.


        """
        if body in SKIP_IN_PATH:
            raise ValueError("Empty value passed for a required argument 'body'.")

        return await self.transport.perform_request(
            "PATCH",
            "/_plugins/_security/api/nodesdn",
            params=params,
            headers=headers,
            body=body,
        )
