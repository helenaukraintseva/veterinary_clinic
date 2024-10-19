from api.models import Pet, User, MedicalHistory


def get_pet_by_user(user: User) -> Pet:
    pet = Pet.objects.filter(user=user).first()

    return pet


def get_medical_history_by_pet(pet_id: str) -> MedicalHistory:
    medical_history = MedicalHistory.objects.filter(pet__id=pet_id)

    return medical_history.all()
