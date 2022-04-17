import graphene

from graphene_django import DjangoObjectType

from ToDoapp.models import Project, TODO
from users.models import User
from uuid import uuid4


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(graphene.ObjectType):
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(TODOType)
    users_by_email = graphene.Field(UserType, email=graphene.String(required=True))
    # todo_by_uid = graphene.Field(TODOType, uid=graphene.UUID(required=True))
    todo_by_is_active = graphene.List(TODOType, is_active=graphene.Boolean(required=True))

    # def resolve_todo_uid(self, info, uid):
    #     try:
    #         return TODO.objects.get(pk=uid)
    #     except TODO.DoesNotExist:
    #         return None

    def resolve_todo_by_is_active(self, info, is_active):
        return TODO.objects.filter(is_active=is_active)

    def resolve_all_todos(root, info):
        return TODO.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_users_by_email(root, info, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)

# class TODOMutation(graphene.Mutation):
#     class Arguments:
#         is_active = graphene.Boolean(required=True)
#         uid = graphene.UUID(required=True)
#
#     todo = graphene.Field(TODOType)
#
#     @classmethod
#     def mutate(cls, root, info, is_active, uid):
#         todo = TODO.objects.get(pk=uid)
#         todo.is_active = is_active
#         todo.save()
#         return TODOMutation(todo=todo)
#
#
# class Mutation(graphene.ObjectType):
#     update_todo = TODOMutation.Field()
#
#
# schema = graphene.Schema(query=Query, mutation=Mutation)
